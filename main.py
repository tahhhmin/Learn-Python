import json, re

with open("cleaned_extracted_text.json", "r", encoding="utf-8") as file:
    cleaned_extracted_data = json.load(file)

finalised_data = []

for i in range(len(cleaned_extracted_data)):

    text = cleaned_extracted_data[i]["text"]
    text_list = text.splitlines()
    word = text_list[1] 
    grammar = text_list[2]
    if len(grammar) > 1:
        grammar = grammar.split()
        grammar = [item for item in grammar if item != "/" ]

    pronounciation = text_list[3]

    extracted_meaning = text.split("meaning")[1].split("usage")[0].strip()
    meanings = re.split(r'(?m)^\s*\d+\.\s*', extracted_meaning)
    meanings = [m.replace("\n", "").strip() for m in meanings if m.strip()]

    extracted_usage = text.split("usage", 1)[1].strip()
    usages = re.split(r'(?m)^\s*\d+\.\s*', extracted_usage)
    usages = [u.replace("\n", "").strip() for u in usages if u.strip()]

    finalised_data.append({
        "id": cleaned_extracted_data[i]["page"],
        "word": word,
        "grammar": grammar,
        "pronounciation": pronounciation,
        "meaning": meanings,
        "usage": usages,
    })

with open("finalised_data.json", "w", encoding="utf-8") as file:
    json.dump(finalised_data, file, ensure_ascii=False, indent=4)