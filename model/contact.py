from exception.exceptions import input_error, WrongEmailFormatException, WrongPhoneNumberFormatException
from util.validation_util import ValidationUtil


class Contact:
    def __init__(self, name, phone, email, address, birthday):
        self.name = name
        self.__phone = phone
        self.__email = email
        self.address = address
        self.birthday = birthday

    @property
    def phone(self):
        return self.__phone

    @input_error
    @phone.setter
    def phone(self, phone):
        if not ValidationUtil.validate_phone(phone):
            raise WrongPhoneNumberFormatException
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @input_error
    @email.setter
    def email(self, email):
        if not ValidationUtil.validate_email(email):
            raise WrongEmailFormatException
        self.__email = email
