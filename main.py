from add import *
from contacts import *
def menu():
    print("=== menu ===")
    print("for add contacts press 1")
    print("to view contacts press 2")
    print("for exit press 0")
    return input("choose ")



while True:
    choice = menu()
    if choice == "0":
        print("closing")
        break


    if choice == "1":
        name = input("Enter a mame ")
        phone = input("Enter a phone number ")
        a1 = AddContacts(name, phone)
        add_contacts(name, phone)


    if choice == "2":
        show_contacts("contacts.txt")


    else:
        print("your choice not legal")
