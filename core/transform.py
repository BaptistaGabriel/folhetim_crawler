import fitz
import pytesseract
from PIL import Image
from openai import OpenAI
import json
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gabri\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

client = OpenAI(base_url="http://localhost:1234/v1")


def fix_hyphenation(text):
    return re.sub(r'-\s*\n\s*', '', text)


def extract_metadata_with_llm(full_text):

    if len(full_text) > 4000:
        context_text = full_text[:2500] + "\n[...] (CONTEÚDO INTERMEDIÁRIO OMITIDO) [...]\n" + full_text[-1500:]
    else:
        context_text = full_text

    prompt = f"""Você é um bibliotecário e historiador especializado em Educação Matemática. 
Catalogar o 'Folhetim' do NEMOC (Núcleo de Educação Matemática Omar Catunda).

### INSTRUÇÕES DE EXTRAÇÃO (CRITICAL):
1. 'publication_year': Procure expressamente por "Ano 1", "Ano 2", etc., no cabeçalho. 
   - Formato de saída: "Ano X" (onde X é o numeral). 
   - ATENÇÃO: Não coloque o ano civil (ex: 1993) aqui. Se não encontrar "Ano X", retorne "000".
2. 'publication_date': Normalize rigorosamente para "Mês abrev. / Ano" (ex: Jan. / 1994) ou intervalos (ex: Mar. - Abr. / 1995).

### REGRAS PARA O RESUMO ('summary'):
- TEMA: Sintetize o foco pedagógico, histórico ou os problemas de matemática abordados.
- ESTILO: Narrativa formal. Inicie alternando entre as expressões: "Esta edição aborda" ou "Este número explora" ou "A presente edição analisa" ou "Este volume examina" ou "Esta edição traz".
- PROIBIÇÕES: Não cite a UEFS, endereços ou o objetivo geral do NEMOC. Foque no conteúdo específico deste número.
- LIMITE: Entre 260 e 310 caracteres. Resumos com menos de 250 ou mais de 310 caracteres serão rejeitados.

TEXTO DO FOLHETIM PARA ANÁLISE:
{context_text}

Responda estritamente no formato JSON:
"""
    try:
        completion = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system",
                 "content": "Você é um especialista em extração de dados JSON. Nunca adicione texto fora do bloco JSON."},
                {"role": "user", "content": prompt}
            ],

            temperature=0.2,
            max_tokens=600,
            presence_penalty=0.2
        )

        content = completion.choices[0].message.content.strip()
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()

        return json.loads(content)
    except Exception as e:
        print(f"      ! Erro no LLM (Folhetim): {e}")
        return {
            "publication_year": "000",
            "publication_date": "Desconhecido",
            "summary": "Erro na geração do resumo técnico."
        }


def extract_text_and_metadata(pdf_path, folhetim_number):
    try:
        doc = fitz.open(pdf_path)
        raw_texts = []

        if 0 <= folhetim_number <= 44 and len(doc) >= 2:
            mapping = [
                (0, 2), (1, 0), (1, 1), (1, 2), (0, 0), (0, 1)
            ]
            for page_idx, col_idx in mapping:
                page = doc[page_idx]
                w, h = page.rect.width, page.rect.height
                col_w = w / 3
                clip = fitz.Rect(col_idx * col_w, 0, (col_idx + 1) * col_w, h)
                pix = page.get_pixmap(clip=clip, dpi=300)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text = pytesseract.image_to_string(img, lang='por')
                raw_texts.append(fix_hyphenation(text))
        else:
            for page in doc:
                pix = page.get_pixmap(dpi=300)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text = pytesseract.image_to_string(img, lang='por')
                raw_texts.append(fix_hyphenation(text))

        doc.close()
        full_text = "\n\n".join(raw_texts)

        print(f"   -> Solicitando metadados e resumo ao LLM...")
        meta = extract_metadata_with_llm(full_text)

        return (
            full_text,
            str(meta.get("publication_year", "000")),
            str(meta.get("publication_date", "Desconhecido")),
            str(meta.get("summary", "Sem resumo."))
        )
    except Exception as e:
        print(f"Erro na extração: {e}")
        return "", "Erro", "Erro", "Erro"