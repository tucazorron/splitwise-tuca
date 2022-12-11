friends = []
expenses = {}

def add_expense():
    print("\n# add expense")
    name = input("Enter name: ")
    amount = input("Enter amount: ")
    if name in expenses:
        expenses[name] += int(amount)
    else:
        expenses[name] = int(amount)

def add_friend():
    print("\n# add friend")
    name = input("Enter name: ")
    friends.append(name)

def menu():
    while True:
        print("\n# splitiwise")
        print("1. add friend")
        print("2. add expense")
        print("3. show friends")
        print("4. show expenses")
        print("5. edit friend")
        print("6. edit expense")
        print("7. exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_friend()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_friends()
        elif choice == "4":
            show_expenses()
        elif choice == "5":
            edit_friend()
        elif choice == "6":
            edit_expense()
        elif choice == "7":
            break
        else:
            print("Invalid choice")

menu()