

import random

while True:
    try:
        randomLimit = int(input())
        if randomLimit < 1:
            continue 
        number = random.randint(1, randomLimit)
    
    except (ValueError, EOFError):
        print("Invalid input. Try again.")
        continue

    while True:
     try:
        guessNum = int(input("Guess: "))
        if guessNum < number:
            print("Too small!")
            continue
        elif guessNum > number:
            print("Too large!")
            continue
        elif guessNum == number:
            print("Just right")
            break
        
     except (ValueError, EOFError):
         continue
    
    break


