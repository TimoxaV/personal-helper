from pprint import pprint

from service.storage_service import StorageService
from service.contact_book import ContactBook
from service.note_book import NoteBook


def main():
    storage = StorageService()
    contact_book = ContactBook(storage)
    note_book = NoteBook(storage)

    commands = {
        "1": ("Add Contact", lambda: add_contact(contact_book)),
        "2": ("Search Contact", lambda: search__contacts(contact_book)),
        "3": ("Edit Contact", lambda: edit_contact(contact_book)),
        "4": ("Delete Contact", lambda: delete_contact(contact_book)),
        "5": ("Birthdays", lambda: birthdays(contact_book)),
        "6": ("Get all Contacts", lambda: get_all_contacts(contact_book)),
        "7": ("Save Contacts", lambda: save__contacts(contact_book)),
        "8": ("Add Note", lambda: add_note(note_book)),
        "9": ("Search Note", lambda: search_note(note_book)),
        "10": ("Edit Note", lambda: edit_note(note_book)),
        "11": ("Delete Note", lambda: delete_note(note_book)),
        "12": ("Add Tag", lambda: add_tag(note_book)),
        "13": ("Remove Tag", lambda: remove_tag(note_book)),
        "14": ("Sort Notes by Tag", lambda: sort_by_tag(note_book)),
        "15": ("Get all Notes", lambda: get_all_notes(note_book)),
        "16": ("Save Notes", lambda: save_notes(note_book)),
        "0": ("Exit", None)
    }

    while True:
        print("\nPersonal helper menu:")
        for k, v in commands.items():
            print(f"{k}. {v[0]}")
        choice = input("Select an option: ")

        if choice == "0":
            break

        action = commands.get(choice)
        if action:
            try:
                action[1]()
            except Exception as e:
                print("Error: ", e)
        else:
            print("Wrong option was selected")


# ==== Contacts ====

def add_contact(contact_book):
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    address = input("Address: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    contact_book.add_contact(name, phone, email, address, birthday)
    print("Contact was added")


def search__contacts(contact_book):
    keyword = input("Enter search keyword: ")
    results = contact_book.search__contacts(keyword)
    for contact in results:
        print(contact)


def edit_contact(contact_book):
    name = input("Find by name: ")
    phone = input("New phone number (press Enter to skip): ")
    email = input("New email (press Enter to skip): ")
    address = input("New address (press Enter to skip): ")
    birthday = input("New birthday (press Enter to skip): ")
    contact_book.edit_contact(name, phone=phone, email=email, address=address, birthday=birthday)
    print("Contact was updated successfully")


def delete_contact(contact_book):
    name = input("Name: ")
    contact_book.delete_contact(name)
    print("Contact was deleted")


def birthdays(contact_book):
    days = int(input("Number of days to search within: "))
    for contact in contact_book.birthdays_in_days(days):
        print(f"{contact.name} — {contact.birthday}")


def get_all_contacts(contact_book):
    pprint(contact_book.get_all__contacts())


def save__contacts(contact_book):
    contact_book.save()


# ==== Notes ====

def add_note(note_book):
    title = input("Name: ")
    text = input("Text: ")
    tags = input("Enter Tags separated by space (press Enter to skip): ").split(" ")
    note_book.add_note(title, text, tags)
    print("Note added")


def search_note(note_book):
    keyword = input("Enter search keyword: ")
    results = note_book.search_notes(keyword)
    for note in results:
        print(note)


def edit_note(note_book):
    title = input("Find by name: ")
    text = input("New text: ")
    note_book.edit_note(title, text)
    print("The note was updated")


def delete_note(note_book):
    title = input("Name: ")
    note_book.delete_note(title)
    print("Note was deleted")


def save_notes(note_book):
    note_book.save()


def add_tag(note_book):
    title = input("Find by title: ")
    tag = input("Tag: ")
    note_book.add_tag(title, tag)
    print("Tag was added")


def remove_tag(note_book):
    title = input("Find by title: ")
    tag = input("Tag: ")
    print(note_book.remove_tag(title, tag))


def sort_by_tag(note_book):
    tag = input("Tag: ")
    pprint(note_book.sort_by_tag(tag))

def get_all_notes(note_book):
    pprint(note_book.get_all_notes())

if __name__ == "__main__":
    main()
