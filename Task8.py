contacts = []

# 1. Add a New Contact:
def add_contact():
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email address: ")
    contact = [name, phone, email]
    contacts.append(contact)
    print("Contact added.\n")

# 2. View All Contacts
def view_contact():
    for x in range(len(contacts)):
        print(x+1, contacts[x][0], "-", contacts[x][1], "-", contacts[x][2])
    print()

# 3. Search for a Contact
def search_contact():
    word = input("Search by name or phone: ")
    for i in contacts:
        if word in i[0] or word in i[1]:
            print(i[0], "-", i[1], "-", i[2])
    print()

# 4. Delete a Contact
def delete_contact():
    word = input("Delete by name or phone: ")
    for y in contacts:
        if word in y[0] or word in y[1]:
            contacts.remove(y)
            print("Contact deleted.\n")
            return
    print("Not found.\n")

# Menu 
while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid option\n")