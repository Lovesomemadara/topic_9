stroke: str = input().strip()

is_num: bool = True

if stroke.startswith("+") or stroke.startswith("-"):
    stroke = stroke[1:]

if "." in stroke:
    if (stroke.count(".") == 1
            and (stroke.replace(".", "")).isdigit()):
        print(True)
    else:
        print(False)
else:
    if stroke.isdigit():
        print(True)
    else:
        print(False)

print(is_num)
