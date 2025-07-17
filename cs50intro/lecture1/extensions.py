# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

# Run your program with python extensions.py. Type happy.jpg and press Enter. Your program should output:
# image/jpeg   
# Run your program with python extensions.py. Type document.pdf and press Enter. Your program should output:
# application/pdf
# Be sure to test each of the other file formats, vary the casing of your input, and “accidentally” add spaces on either side of your input before pressing enter.
# Your program should behave as expected, case- and space-insensitively.

extensionsIn = input("File name:")
extensions = extensionsIn.strip().lower()

gif =".gif"
jpg =".jpg"
jpeg = ".jpeg"
png = ".png"
pdf = ".pdf"
txt = ".txt"
zip = ".zip"

if extensions.endswith(gif):
    print("image/gif")

elif extensions.endswith(jpg):
    print("image/jpeg")

elif extensions.endswith(jpeg):
    print("image/jpeg")

elif extensions.endswith(png):
    print("image/png")

elif extensions.endswith(pdf):
    print("application/pdf")

elif extensions.endswith(txt):
    print("text/plain")

elif extensions.endswith(zip):
    print("application/zip")

else:
    print("application/octet-stream")
