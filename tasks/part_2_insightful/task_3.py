string: str = input()
clean_string: str = ''.join(char.lower()
                            for char in string if char.isalnum())

print(clean_string == clean_string[::-1])
