# Структура імпортів проекту

## 📊 Граф залежностей між модулями

```
test.py (ТОЧКА ВХОДУ)
  ├── import service.contact_book
  │   └── ContactBook class
  ├── import util.validation_util
  │   └── ValidationUtil class
  └── import exception.exceptions
      ├── ContactNotFoundException
      ├── WrongEmailFormatException
      └── WrongPhoneNumberFormatException

model/contact_book.py
  ├── import model.contact
  │   └── Contact class
  ├── import util.validation_util
  │   └── ValidationUtil.validate_phone()
  │   └── ValidationUtil.validate_email()
  ├── import exception.exceptions
  │   ├── ContactNotFoundException
  │   ├── WrongEmailFormatException
  │   └── WrongPhoneNumberFormatException
  ├── import pickle (stdlib)
  ├── import os (stdlib)
  ├── import datetime (stdlib)
  └── import pathlib (stdlib)

model/contact.py
  ├── import datetime (stdlib)
  ├── import pathlib (stdlib)
  ├── import util.validation_util
  │   ├── ValidationUtil.validate_phone()
  │   └── ValidationUtil.validate_email()
  └── import exception.exceptions
      ├── WrongEmailFormatException
      └── WrongPhoneNumberFormatException

util/validation_util.py
  └── import re (stdlib)
      └── (нема залежностей від своїх модулів)

exception/exceptions.py
  └── (нема залежностей)
```

---
