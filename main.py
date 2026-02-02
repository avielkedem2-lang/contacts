from add import *
from contacts import *
def menu():
    print("=== menu ===")
    print("for add contacts press 1")
    print("to view contacts press 2")
    print("for search contact press 3")
    print("for delete contact press 4")
    print("for edit contact press 5")
    print("for exit press 0")
    return input("choose ")



while True:
    choice = menu()
    if choice == "0":
        print("closing")
        break


    elif choice == "1":
        name = input("Enter a mame ")
        phone = input("Enter a phone number ")
        a1 = AddContacts(name, phone)
        add_contacts(name, phone)


    elif choice == "2":
        show_contacts("contacts.txt")


    elif choice == "3":
        x = input("Enter a name to search for ")
        print(search_contacts(x))


    elif choice == "4":
        x = input("Enter a name to delete for ")
        deleting_contact(x)


    elif choice == "5":
        name = input("Enter the mame ")
        phone = input("Enter the new phone number ")
        number_update(name, phone)


    else:
        print("your choice not legal")
