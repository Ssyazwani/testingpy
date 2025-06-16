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
  
    first_digit_index = None
    for i, ch in enumerate(s):
        if ch.isdigit():
            first_digit_index = i
            break

    if first_digit_index is not None:
      
        if s[first_digit_index] == '0':
            return False
      
        if not s[first_digit_index:].isdigit():
            return False

    return True



#  “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters 
# (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; 
# they must come at the end. 
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
    ...


main()