import json, re

cleaned_data = []
needed = [1, 2, 203, 204, 404, 605, 806, 1007, 1208]
needed_fixed = []
for i in needed:
    needed_fixed.append(i - 1)

with open("raw_extracted_text.json", "r", encoding="utf-8") as file:
    raw_extracted_data = json.load(file)

num = 0

for i in range(len(raw_extracted_data)):
    if not i in needed_fixed:
        cleaned_data.append({
            "page": num,
            "text": raw_extracted_data[i]["text"]
        })
        num += 1

with open("cleaned_extracted_text.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)