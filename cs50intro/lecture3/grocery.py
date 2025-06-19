grocery_list ={}

try: 
  while True:
   item = input().strip().upper()

   if item in grocery_list:
     grocery_list[item] += 1

   else:
     grocery_list[item] =1


except EOFError:
   print()

   for item in grocery_list:
      print(f"{grocery_list[item]} {item}")


