from fractions import Fraction

def main():
 x = get_frac("Fraction:")
 print(x)


def get_frac(prompt):
     while True:
        try:
            value = Fraction(input(prompt)) 
            percent = round(value * 100)

            if percent <= 1:
                return "E"
            elif percent >= 99:
                return "F"
            else:
                return percent

        except (ValueError, ZeroDivisionError):
          pass

main()