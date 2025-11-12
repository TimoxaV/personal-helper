import sys
import os
import pickle
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from util.validation_util import ValidationUtil
from exception.exceptions import (
    ContactNotFoundException,
    WrongEmailFormatException,
    WrongPhoneNumberFormatException
)
from model.contact import Contact


class ContactBook:
    def __init__(self):
        self.__contacts = {}

    def add_contact(self, name, phone, email, address, birthday):
        if name in self.__contacts:
            raise ContactNotFoundException(f"Contact '{name}' already exists.")

        if not ValidationUtil.validate_phone(phone):
            raise WrongPhoneNumberFormatException("Invalid phone format")

        if not ValidationUtil.validate_email(email):
            raise WrongEmailFormatException("Invalid email format")

        try:
            birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use YYYY-MM-DD."

        contact = Contact(name, phone, email, address, birthday_date)
        self.__contacts[name] = contact
        return f"Contact '{name}' successfully added."

    def edit_contact(self, name, phone=None, email=None, address=None, birthday=None):
        if name not in self.__contacts:
            raise ContactNotFoundException("Contact not found")
        
        contact = self.__contacts[name]
        
        if phone:
            if not ValidationUtil.validate_phone(phone):
                raise WrongPhoneNumberFormatException("Invalid phone format")
            contact.phone = phone
        
        if email:
            if not ValidationUtil.validate_email(email):
                raise WrongEmailFormatException("Invalid email format")
            contact.email = email
        
        if address:
            contact.address = address
        
        if birthday:
            try:
                contact.birthday = datetime.strptime(birthday, "%Y-%m-%d")
            except ValueError:
                return "Invalid date format. Use YYYY-MM-DD."
        
        return f"Contact '{name}' updated successfully."

    def search_contacts(self, keyword):
        keyword = keyword.lower()
        results = []

        for contact in self.__contacts.values():
            if (
                keyword in contact.name.lower()
                or keyword in contact.email.lower()
                or keyword in contact.phone
                or keyword in contact.address.lower()
            ):
                results.append(contact)

        return results

    def get_all_contacts(self):
        return list(self.__contacts.values())

    def get_contact(self, name):
        if name not in self.__contacts:
            raise ContactNotFoundException("Contact not found")
        return self.__contacts[name]

    def delete_contact(self, name):
        if name not in self.__contacts:
            raise ContactNotFoundException("Contact not found")
        del self.__contacts[name]
        return f"Contact '{name}' deleted."

    def save(self, filename="contacts.pkl"):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self.__contacts, f)
            return f"Contacts saved to {filename}"
        except Exception as e:
            return f"Error saving contacts: {str(e)}"

    def load(self, filename="contacts.pkl"):
        try:
            if os.path.exists(filename):
                with open(filename, "rb") as f:
                    self.__contacts = pickle.load(f)
                return f"Contacts loaded from {filename}"
            else:
                return f"File {filename} not found."
        except Exception as e:
            return f"Error loading contacts: {str(e)}"

    def __str__(self):
        if not self.__contacts:
            return "No contacts found."
        return "\n".join(str(c) for c in self.__contacts.values())