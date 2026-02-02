list_contacts = []
def add_contacts(name, phone_number):
    save = f"name: {name}, phone number: {phone_number}"
    list_contacts.append(save)

    try:
        with open("contacts.txt", "a") as f:
            f.write("\n")
            f.write(save)
    except Exception as error:
        print(error)


def show_contacts(fils_txt):
    try:
        with open(fils_txt) as f:
            print(f.read())
    except Exception as fild:
        print(fild)


def search_contacts(name):
    try:
        with open("contacts.txt") as fil:
            for f in fil.readlines():
                if name in f:
                    return f
            return "contact not fund"
    except Exception as fild:
        print(fild)


def deleting_contact(name):
    try:
        new_lines = []
        with open("contacts.txt") as fil:
            for f in fil.readlines():
                if name not in f:
                    new_lines.append(f)
        x = input("are you sure you want to delete ")
        if x == "yes":
            with open("contacts.txt", "w") as file:
                file.writelines(new_lines)
            print("the contact is delete")
        else:
            print("the contact is not deleted")

    except Exception as fild:
        print(fild)