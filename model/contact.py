import sys
import os
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from exception.exceptions import input_error, WrongEmailFormatException, WrongPhoneNumberFormatException
from util.validation_util import ValidationUtil


class Contact:
    def __init__(self, name, phone, email, address, birthday):
        self.name = name
        self._phone = phone
        self._email = email
        self.address = address
        self.birthday = birthday

    # Phone getter
    @property
    def phone(self):
        return self._phone

    # Phone setter
    @phone.setter
    def phone(self, value):
        if not ValidationUtil.validate_phone(value):
            raise WrongPhoneNumberFormatException("Invalid phone format")
        self._phone = value

    # Email getter
    @property
    def email(self):
        return self._email

    # Email setter
    @email.setter
    def email(self, value):
        if not ValidationUtil.validate_email(value):
            raise WrongEmailFormatException("Invalid email format")
        self._email = value

    def __str__(self):
        return f"{self.name}: {self._phone}, {self._email}, {self.address}, {self.birthday.date()}"