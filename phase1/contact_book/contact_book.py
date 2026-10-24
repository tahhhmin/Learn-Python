import json
from pathlib import Path

def read_contacts():
    file_path = Path(__file__).parent / "contacts.json"
    
    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        print("Cant find file in path. Creating local list.")
        contacts = []

    return contacts

contacts = read_contacts()
print(json.dumps(contacts, indent=4))