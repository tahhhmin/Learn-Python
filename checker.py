import json

data = []

with open("finalised_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(len(data))