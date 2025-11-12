import re


class ValidationUtil:

    @staticmethod
    def validate_phone(phone):
        return re.fullmatch(r"\+?\d{10,15}", phone)

    @staticmethod
    def validate_email(email):
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email)
