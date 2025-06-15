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
gif = ".gif"
jpg = ".jpg"
jpeg = ".jpeg"
png = ".png"
pdf= ".pdf"
txt = ".txt"
zip = ".zip"

if gif in extensionsIn:
    print("image/gif")

elif jpg in extensionsIn:
    print("image/jpg")

elif jpeg in extensionsIn:
    print("image/jpeg")

elif png in extensionsIn:
    print("image/png")

elif pdf in extensionsIn:
    print("application/pdf")

elif txt in extensionsIn:
    print("text/plain")

elif zip in extensionsIn:
    print("application/zip")

else:
    print("application/octet-stream")