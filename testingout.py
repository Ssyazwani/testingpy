# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
# name = input("What's your name? ").strip().title()

# # Print the output
# print(f"hello, {name}")

# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()