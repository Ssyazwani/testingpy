names = []

try:
    while True:
        name = input("Enter a name: ")
        names.append(name)

        
except EOFError:

    def format_names(names):
     if len(names) == 1:
        return names[0]
     elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
     elif len(names) >=3:
        return ", ".join(names[:-1]) + ", and " + names[-1]

print("Adieu, adieu, to " + format_names(names))

    
