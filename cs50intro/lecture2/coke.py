total = 0

while total < 50:
    num = int(input("Insert coin:")) 

    if num not in [5,10,25]:
        print("Amount owed:"+ str((50 - total)))
        continue

    total += num

    if total > 50:
        print("Change owed:"+ str((total-50)))
        break
    else:
        print("Amount owed:"+ str((50-total)))
    


