ALPHABETS: dict[str, str] = {
    "vowels": "АЕЁИОУЫЭЮЯаеёиоуыэюяAEIOUaeiou",
    "constants": "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
                 "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬбвгджзйклмнпрстфхцчшщъь"
}

vowels_count: int = 0
constants_count: int = 0
for let in input():
    if let in ALPHABETS["vowels"]:
        vowels_count += 1
    elif let in ALPHABETS["constants"]:
        constants_count += 1

print(f'{vowels_count}\n{constants_count}')
