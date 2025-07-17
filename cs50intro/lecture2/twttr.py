# (A, E, I, O, and U)

yourInput = input("Input: ")

cleaned = ""

for char in yourInput:
     if char not in ['a','A', 'e','E', 'i','I', 'o','O','u','U']:
        cleaned += char

print("Output: " + cleaned)
