# Student Contact Manager

contacts = {}

emails = set()
phones = set()


def add_contact():
    student_id = input("Enter Student ID or Email: ")

    if student_id in contacts:
        print("This contact already exists.")
        return

    name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    role = input("Enter Role (Student/Parent/Teacher): ")

    if email in emails:
        print("This email already exists.")
        return

    if phone in phones:
        print("This phone number already exists.")
        return

    contacts[student_id] = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Role": role
    }

    emails.add(email)
    phones.add(phone)

    print("Contact added successfully!")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("\nContact List")
        for student_id, details in contacts.items():
            print("-------------------------")
            print("ID:", student_id)
            print("Name:", details["Name"])
            print("Email:", details["Email"])
            print("Phone:", details["Phone"])
            print("Role:", details["Role"])


def search_contact():
    student_id = input("Enter Student ID or Email to search: ")

    if student_id in contacts:
        details = contacts[student_id]
        print("\nContact Found")
        print("Name:", details["Name"])
        print("Email:", details["Email"])
        print("Phone:", details["Phone"])
        print("Role:", details["Role"])
    else:
        print("Contact not found.")


def update_contact():
    student_id = input("Enter Student ID or Email to update: ")

    if student_id not in contacts:
        print("Contact not found.")
        return

    old_email = contacts[student_id]["Email"]
    old_phone = contacts[student_id]["Phone"]

    name = input("Enter New Name: ")
    email = input("Enter New Email: ")
    phone = input("Enter New Phone: ")
    role = input("Enter New Role: ")

    if email != old_email and email in emails:
        print("Email already exists.")
        return

    if phone != old_phone and phone in phones:
        print("Phone number already exists.")
        return

    emails.remove(old_email)
    phones.remove(old_phone)

    emails.add(email)
    phones.add(phone)

    contacts[student_id] = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Role": role
    }

    print("Contact updated successfully!")


def delete_contact():
    student_id = input("Enter Student ID or Email to delete: ")

    if student_id in contacts:
        emails.remove(contacts[student_id]["Email"])
        phones.remove(contacts[student_id]["Phone"])

        del contacts[student_id]

        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


while True:

    print("\n===== Student Contact Manager =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
