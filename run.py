from core.load import setup_storage, save_newsletter, is_already_indexed
from core.extract import download_pdf
from core.transform import extract_text_and_metadata
import time


def main():
    setup_storage()

    for i in range(0, 171):
        if is_already_indexed(i):
            print(f"Folhetim {i} já processado")
            continue

        print(f"\n[Folhetim {i}]")
        pdf_path, url = download_pdf(i)

        if pdf_path:
            content, ed_year, pub_date, summary = extract_text_and_metadata(pdf_path, i)

            if content.strip():
                save_newsletter(i, ed_year, pub_date, summary, url, content)
                print(f"Salvo: Ano {ed_year} | {pub_date}")
            else:
                print(f"Conteúdo vazio.")
        else:
            print(f"PDF não encontrado.")

        time.sleep(1)


if __name__ == "__main__":
    main()