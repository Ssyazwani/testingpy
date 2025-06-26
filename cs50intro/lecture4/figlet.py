from pyfiglet import Figlet, FigletFont
import sys

args = sys.argv[1:]

if len(args) == 0:
    font = 'standard'  

elif len(args) == 2 and args[0] in ['-f', '--font']:
    font = args[1]
    if font not in Figlet().getFonts():
        sys.exit("Invalid Usage")
else:
    sys.exit("Usage: python figlet.py [-f FONT_NAME]")


figlet = Figlet(font = font)
text = input("Input: ")
print("Output:")
print(figlet.renderText(text))

