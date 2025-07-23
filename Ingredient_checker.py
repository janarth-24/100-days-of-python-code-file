# Ingredients Checker

#Define a one recipe ingreditens
required_ingredient={"egg",'onion',"spices","oil","tomato","water"}

#Get user availabe ingredient as input
user_ingredient=input("Enter the ingredient you have (separated by commas) :")
user_ingredient=set(user_ingredient.split(","))

#compare the Ingredient
missing_ingredient=required_ingredient-user_ingredient
extra_ingredient=user_ingredient-required_ingredient

#Show the result and recommend some recipes using this user ingredient
print("\n--- Ingredient Check Results ----")
if missing_ingredient:
    print(f"You are missing following ingredient {",".join(missing_ingredient)}")
else:
    print("You have all needed ingredient")
if extra_ingredient:
    print(f"You have extra ingredients: {', '.join(extra_ingredient)}")
else:
    print("You have all the ingredients needed.")
print("\n--- Suggested Recipe ----")
if "egg"and"onion"and"spices" in user_ingredient:
    print("You may prepare a omelette")
elif "milk" and "water":
    print("You may prepare a hot cup of milk")
elif "egg"and"onion"and"spices" and "bread" in user_ingredient:
    print("You may prepare a Bread omelette")
elif user_ingredient==required_ingredient:
    print("You can prepare Eggcurry")