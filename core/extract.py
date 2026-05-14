import requests
import os

def download_pdf(number):
    os.makedirs("data/raw", exist_ok=True)
    num_str = str(number).zfill(3)
    url = f"http://www.nemoc.uefs.br/arquivos/File/Folhetim/Folhetim{num_str}.pdf"
    pdf_path = f"data/raw/folhetim_{num_str}.pdf"

    if os.path.exists(pdf_path):
        return pdf_path, url

    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            return pdf_path, url
    except Exception as e:
        print(f"Erro no download do folhetim {number}: {e}")
    return None, None