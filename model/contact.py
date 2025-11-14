from datetime import datetime, date

from exception.exceptions import WrongEmailFormatException, WrongPhoneNumberFormatException
from util.validation_util import ValidationUtil


class Contact:
    def __init__(self, name, phone, email, address, birthday: date):
        self.name = name
        self._phone = phone
        self._email = email
        self.address = address
        self.birthday = birthday

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self._phone,
            "email": self._email,
            "address": self.address,
            "birthday": self.birthday.strftime("%Y-%m-%d")
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            address=data["address"],
            birthday=datetime.strptime(data["birthday"], "%Y-%m-%d").date()
        )

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not ValidationUtil.validate_phone(value):
            raise WrongPhoneNumberFormatException("Invalid phone format")
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not ValidationUtil.validate_email(value):
            raise WrongEmailFormatException("Invalid email format")
        self._email = value

    def __str__(self):
        return f"{self.name}: {self._phone}, {self._email}, {self.address}, {self.birthday}"

    def __repr__(self):
        return f"Contact({self.__str__()})"
