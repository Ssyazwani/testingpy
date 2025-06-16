
fruit_cal = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}



fruit = input("Item: ").strip().lower()  # Prompt and input on same line

while fruit not in fruit_cal:
    fruit = input().lower()

print("Calories:"+ str(fruit_cal[fruit])) 





# if fruit not in fruit_cal:
#         continue 


# if fruit in fruit_cal:
#         print("Calories:"+ str(fruit_cal[fruit]))
#      break  


# Apple
# 	130	
# Avocado
# 	50	
# Banana
# 	110	
# Cantaloupe
# 	50	
# Grapefruit
# 	60	
# Grapes
# 90	
# Honeydew 
# Melon
# 	50	
# Kiwifruit
# 90	
# Lemon
# 	15	
# Lime
# 	20	
# Nectarine
# 	60	
# Orange
# 80	
# Peach
# 	60	
# Pear
# 100	
# Pineapple
# 	50	
# Plums
# 	70	
# Strawberries
# 	50	
# Sweet
# Cherries
# 	100	
# Tangerine
# 	50	
# Watermelon
# 	80