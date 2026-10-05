import csv
from pathlib import Path
import pymupdf

# Project root = behaviour-guide/
BASE_DIR = Path(__file__).resolve().parents[2]

SOURCES_FILE = BASE_DIR / "data" / "sources.csv"
RAW_DIR = BASE_DIR / "data" / "raw"


with open(SOURCES_FILE, "r", encoding="utf-8", newline="") as file:
    sources = csv.DictReader(file)

    for source in sources:
        source_id = source["id"]
        title = source["title"]
        filename = source["filename"]

        pdf_path = RAW_DIR / filename

        print("\n" + "=" * 60)
        print(f"Source ID: {source_id}")
        print(f"Title: {title}")
        print(f"Filename: {filename}")

        if not pdf_path.exists():
            print("ERROR: PDF not found")
            continue

        try:
            # Open PDF without extracting the whole document
            doc = pymupdf.open(pdf_path)

            print(f"Page count: {len(doc)}")

            # Page 5 = index 4
            if len(doc) < 5:
                print("Page 5: PDF has fewer than 5 pages")
            else:
                text = doc[4].get_text()

                if not text.strip():
                    print("SCANNED?")
                else:
                    print("Page 5 sample:")
                    print(text[:150])

            doc.close()

        except Exception as e:
            print(f"ERROR opening PDF: {e}")
