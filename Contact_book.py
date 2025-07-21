#Contact book app
from pycparser.c_ast import While

#initial the contact dictionary
contact={}

#step1: show the menu for the contact app
def show():
    print(f"----Contact book----")
    print(f"1. Add new Contact")
    print(f"2. View Contacts")
    print(f"3. Edit a Contact")
    print(f"4. Search Contact ")
    print(f"5. Delete Contact")
    print(f"6. Exit")

#step 2: Add the new contact
def add_contact():
    name=input("Enter the Name : ")
    phone=int(input("Enter the Phone number : "))
    email=input("Enter the Email Id : ")
    contact[name]={"phone":phone ,"email": email}
    print(f"Contact {name} has been add to contact book successfully")

#step 3: View the Contact book
def view_contact():
    if contact:
        print(f"----Contact List----")
        for name,details in contact.items():
            print(f"Name :{name}")
            print(f"Phone Number :{details['phone']}")
            print(f"Email :{details['email']}")
    else:
        print(f"Your contact book is empty")

#step 4: Edit the existing contact
def edit_contact():
    name=input("Enter the name to be edit :")
    if name in contact:
        phone=int(input("Enter the phone number ;"))
        email=input("Enter the Email :")
        contact[name] = {"phone": phone, "email": email}
        print(f"Contact {name} has been updated to contact book successfully")

#step 5:Search the contact
def search_contact():
    name=input("Enter the name to search from contact list")
    if name in contact:
        print(f"----Contact Details for {name}---")
        print(f"Name :{name}")
        print(f"Phone Number :{contact[name]['phone']}")
        print(f"Email :{contact[name]['email']}")
    else:
        print(f"Contact {name } not found in your contact list")

#step 6:Delete te contact from contact list
def delete_contact():
    name=input("Enter the name to delete from your contact list :")
    if name in contact:
        del contact[name]
        print(f"Contact {name} has been delete successfully")
    else:
        print(f'Contact {name } not found from your contact list')

#step 7:Exit from contact list
def exit_contact():
    print("Your are exit from contact list")

#step 8: Run the program by loop
while True:
    show()
    choice=int(input("Enter the Choice (1-6) :"))
    if choice==1:
        add_contact()
    elif choice==2:
        view_contact()
    elif choice ==3:
        edit_contact()
    elif choice==4:
        search_contact()
    elif choice==5:
        delete_contact()
    elif choice == 6:
        exit_contact()
        break
    else:
        print("Your Entered invaild choice (1-6)")