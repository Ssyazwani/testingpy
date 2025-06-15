# In deep.py, 
# implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
#  outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

deepAns = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")



if deepAns == "42":
 print("Yes")

elif deepAns == "forty-two":
 print("Yes")

elif deepAns == "forty two":
 print("Yes")

else:
 print("No")