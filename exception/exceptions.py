def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ContactNotFoundException:
            return "Contact not found"
        except WrongPhoneNumberFormatException:
            return "Wrong phone number format. Example: +14155552671. The phone may or may not start with plus sign"
        except WrongEmailFormatException:
            return "Wrong email format"
        except NoteNotFound:
            return "Note not found"

    return inner


class ContactNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class WrongPhoneNumberFormatException(Exception):
    def __init__(self, message):
        super().__init__(message)


class WrongEmailFormatException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoteNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
