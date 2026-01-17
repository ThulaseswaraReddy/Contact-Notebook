FILE_NAME = "contacts.txt"
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully")
def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found")
            else:
                print("\n Contact List :")
                for contact in contacts:
                    name, phone, email = contact.strip().split(",")
                    print(f"Name : {name}, Phone : {phone}, Email : {email}")
    except FileNotFoundError:
        print("No contact file found")
def search_contact():
    search_name = input("Enter name to search: ")
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"✅ Found: Name : {name}, Phone : {phone}, Email : {email}")
                    found = True
                    break
        if not found:
            print("❌ Contact not found")
    except FileNotFoundError:
        print("No contact file found")
def delete_contact():
    delete_name = input("Enter name to delete: ")
    contacts = []
    deleted = False
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
        with open(FILE_NAME, "w") as file:
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                if name.lower() != delete_name.lower():
                    file.write(contact)
                else:
                    deleted = True
        if deleted:
            print("🗑️ Contact deleted successfully")
        else:
            print("❌ Contact not found")
    except FileNotFoundError:
        print("No contact file found")
def main():
    while True:
        print("\n--- Contact Notebook ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Notebook")
            break
        else:
            print("❌ Invalid choice,Try again.")
main()