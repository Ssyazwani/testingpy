camelInput = input("camelCase: ")
newstring = ""

for char in camelInput:
    if char.isupper():
        newstring += "_" + char
    else:
        newstring += char

print("snake_case:", newstring)
