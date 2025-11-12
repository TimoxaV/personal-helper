import pickle
import os

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = phone
            print(f"Added contact: {name} - {phone}")

    def show_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def edit_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"Updated '{name}' with new phone: {new_phone}")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact '{name}'.")
        else:
            print(f"Contact '{name}' not found.")


def save_data(book):
    with open("contacts.pkl", "wb") as f:
        pickle.dump(book, f)


def load_data():
    if os.path.exists("contacts.pkl"):
        with open("contacts.pkl", "rb") as f:
            return pickle.load(f)
    return AddressBook()


def main():
    book = load_data()

    while True:
        print("\nCommands: add, show, edit, delete, exit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            book.add_contact(name, phone)

        elif command == "show":
            book.show_contacts()

        elif command == "edit":
            name = input("Name to edit: ").strip()
            new_phone = input("New phone: ").strip()
            book.edit_contact(name, new_phone)

        elif command == "delete":
            name = input("Name to delete: ").strip()
            book.delete_contact(name)

        elif command == "exit":
            save_data(book)
            print("Program closed.")
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
