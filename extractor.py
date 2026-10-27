import pymupdf
import json

pdf_path = "vocab.pdf"
pages = []

with pymupdf.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf, start=1):
        text = page.get_text("text")
        text = text.lower()

        pages.append({
            "page": page_number,
            "text": text,
        })

        print(f"Processed page {page_number}/{len(pdf)}")

with open("raw_extracted_text.json", "w", encoding="utf-8") as file:
    json.dump(pages, file, ensure_ascii=False, indent=4)

print("Text extraction complete!")


