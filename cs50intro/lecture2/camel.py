camelInput = input("camelCase: ")
newstring = ""

for char in camelInput:
    if char.isupper():
        newstring += "_" + char.lower()

    else:
        newstring += char

print(newstring)
