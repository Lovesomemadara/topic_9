stroke: str = input()
vowels_count: int = 0
constants_count: int = 0

ALPHABETS = {
    "vowels": "АЕЁИОУЫЭЮЯаеёиоуыэюяAEIOUaeiou",
    "constants": "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
                 "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬбвгджзйклмнпрстфхцчшщъь"
}
vowels: str = ALPHABETS["vowels"]
constants: str = ALPHABETS["constants"]

for i in stroke:
    if i in vowels:
        vowels_count += 1
    elif i in constants:
        constants_count += 1
print(f'{vowels_count}\n{constants_count}')
