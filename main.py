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
    else:
        print("your choice not legal")
