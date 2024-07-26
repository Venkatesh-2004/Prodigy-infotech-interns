import csv

# File name for storing contacts
CONTACTS_FILE = 'contacts.csv'

# Function to display menu
def display_menu():
    print("\nContact Management System")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

# Function to load contacts from CSV file
def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

# Function to save contacts to CSV file
def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        fieldnames = ['Name', 'Phone', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

# Function to view contacts
def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("\nContacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']} - {contact['Email']}")
    else:
        print("\nNo contacts found.")

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts = load_contacts()
    contacts.append({'Name': name, 'Phone': phone, 'Email': email})
    save_contacts(contacts)
    print("\nContact added successfully.")

# Function to update an existing contact
def update_contact():
    contacts = load_contacts()
    view_contacts()
    if contacts:
        idx = int(input("\nEnter the contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            contacts[idx]['Name'] = input("Enter new name: ")
            contacts[idx]['Phone'] = input("Enter new phone: ")
            contacts[idx]['Email'] = input("Enter new email: ")
            save_contacts(contacts)
            print("\nContact updated successfully.")
        else:
            print("\nInvalid contact number.")
    else:
        print("\nNo contacts to update.")

# Function to delete a contact
def delete_contact():
    contacts = load_contacts()
    view_contacts()
    if contacts:
        idx = int(input("\nEnter the contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            contacts.pop(idx)
            save_contacts(contacts)
            print("\nContact deleted successfully.")
        else:
            print("\nInvalid contact number.")
    else:
        print("\nNo contacts to delete.")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()
