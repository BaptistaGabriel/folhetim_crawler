import os
import csv

METADATA_CSV = "data/metadata.csv"
TEXTS_DIR = "data/texts"


def setup_storage():
    os.makedirs(TEXTS_DIR, exist_ok=True)
    if not os.path.exists(METADATA_CSV):
        with open(METADATA_CSV, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["number", "editorial_year", "publication_date", "summary", "url", "text_file"])
    print("Armazenamento CSV + TXT pronto.")


def save_newsletter(number, editorial_year, pub_date, summary, url, content):
    num_str = str(number).zfill(3)
    txt_filename = f"Folhetim{num_str}.txt"
    txt_path = os.path.join(TEXTS_DIR, txt_filename)

    with open(txt_path, mode='w', encoding='utf-8') as f:
        f.write(content)

    with open(METADATA_CSV, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([number, editorial_year, pub_date, summary, url, txt_filename])


def is_already_indexed(number):
    num_str = str(number).zfill(3)
    return os.path.exists(os.path.join(TEXTS_DIR, f"Folhetim{num_str}.txt"))