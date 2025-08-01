def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s.isalnum():
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i]=='0':
                return False
            return s[i:].isdigit()


    return True



main()

#  “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters 
# (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; 
# they must come at the end. 
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
