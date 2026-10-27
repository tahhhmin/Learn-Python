meanings = "\n1.\nmake chemically neutral\n2.\nmake ineffective by counterbalancing the effect of\n3.\nmake incapable of military action\n"
meanings_list = meanings.split()

meaning_counter = 1

meaning = []

for i in meanings_list:
    if i == '1.':
        meaning_counter = 2
    elif i == '3.':
        meaning_counter = 3

if meaning_counter == 3:
    meaning1 = meanings.split("1.")[1].split("2.")[0].strip()
    meaning.append(meaning1)
    meaning2 = meanings.split("2.")[1].split("3.")[0].strip()
    meaning.append(meaning2)
    meaning3 = meanings.split("3.")[1].strip()
    meaning.append(meaning3)
elif meaning_counter == 2:
    meaning1 = meanings.split("1.")[1].split("2.")[0].strip()
    meaning.append(meaning1)
    meaning2 = meanings.split("2.")[1].strip()
    meaning.append(meaning2)
else:
    meaning.append(meanings)

print(f"has {meaning_counter} meaning(s)")
print(meaning)