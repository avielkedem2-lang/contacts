list_contacts = []
def add_contacts(name, phone_number):
    save = f"name: {name}, phone number: {phone_number}"
    list_contacts.append(save)

    try:
        with open("contacts.txt", "a") as f:
            f.write(save)
    except Exception as error:
        print(error)

