# Contact Book Program

contacts = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added!")

    elif choice == "2":
        if not contacts:
            print("No contacts yet.")
        else:
            for i, contact in enumerate(contacts, 1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    elif choice == "3":
        name = input("Enter name to search: ").lower()
        found = False
        for contact in contacts:
            if contact["name"].lower() == name:
                print(f"Found: Name={contact['name']}, Phone={contact['phone']}, Email={contact['email']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to update: ").lower()
        found = False
        for contact in contacts:
            if contact["name"].lower() == name:
                contact["phone"] = input("Enter new phone: ")
                contact["email"] = input("Enter new email: ")
                print("Contact updated!")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter name to delete: ").lower()
        found = False
        for i, contact in enumerate(contacts):
            if contact["name"].lower() == name:
                del contacts[i]
                print("Contact deleted!")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
