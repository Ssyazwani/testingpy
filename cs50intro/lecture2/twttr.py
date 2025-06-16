# (A, E, I, O, and U)

yourInput = input()

cleaned = ""

for char in yourInput:
     if char not in ['a', 'e', 'i', 'o','u']:
        cleaned += char

print(cleaned)
