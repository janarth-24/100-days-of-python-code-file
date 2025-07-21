#Shopping List App
shopping_list=[]
# Shopping List App
def showmenu():
  print("\n------Shoppingt list menu---")
  print("1. Visw the Shopping List ")
  print("2. Add an item ")
  print("3. Remove an item")
  print("4. Clear List")
  print("5. Exit ")


while True:
  showmenu()
  choice =input("Enter your choice(1-5): ")

  if choice == "1":
    print("\n----Shopping list --")
    if not shopping_list:
      print(" Your shopping list is empty")
    else:
      for index, item in enumerate(shopping_list):
        print(f"{index+1}.{item}")

  elif choice =="2":
    item=input("Enter the item to add ")
    shopping_list.append(item)
    print(f"{item} has been added to shopping list")

  elif choice =="3":
    item=input("Enter the item to remove")
    if item in shopping_list:
      shopping_list.remove(item)
      print(f"{item} has been remove from the Shopping list. ")
    else:
      print(f"{item} is not in the shopping list. ")

  elif choice== "4":
    shopping_list.clear()
    print("The shopping list has been cleared.")

  elif choice == "5":
    shopping_list.clear()
    print("Goodbye! Happy Shopping ")

  else:
    print("Invaild choice. Please try again ")