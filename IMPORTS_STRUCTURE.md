# Структура імпортів проекту

## 📊 Граф залежностей між модулями

```
main.py (ТОЧКА ВХОДУ)
  ├── import service.storage_service
  │   └── StorageService class
  ├── import service.contact_book
  │   └── ContactBook class
  └── import service.note_book
      └── NoteBook class

service/contact_book.py
  ├── import datetime (stdlib)
  │   └── datetime, timedelta
  ├── import service.storage_service
  │   └── StorageService class
  ├── import util.validation_util
  │   └── ValidationUtil.validate_phone()
  │   └── ValidationUtil.validate_email()
  ├── import util.date_util
  │   └── is_valid_date()
  ├── import exception.exceptions
  │   ├── ContactNotFoundException
  │   ├── WrongEmailFormatException
  │   └── WrongPhoneNumberFormatException
  └── import model.contact
      └── Contact class

service/note_book.py
  ├── import model.note
  │   └── Note class
  ├── import exception.exceptions
  │   ├── input_error (decorator)
  │   └── NoteNotFound
  └── import service.storage_service
      └── StorageService class

service/storage_service.py
  ├── import json (stdlib)
  ├── import os (stdlib)
  └── (нема залежностей від своїх модулів)

model/contact.py
  ├── import datetime (stdlib)
  │   └── datetime, date
  ├── import exception.exceptions
  │   ├── WrongEmailFormatException
  │   └── WrongPhoneNumberFormatException
  └── import util.validation_util
      ├── ValidationUtil.validate_phone()
      └── ValidationUtil.validate_email()

model/note.py
  └── import datetime (stdlib)
      └── datetime

util/validation_util.py
  └── import re (stdlib)
      └── (нема залежностей від своїх модулів)

util/date_util.py
  ├── import datetime (stdlib)
  │   └── date
  └── (нема залежностей від своїх модулів)

exception/exceptions.py
  └── (нема залежностей від інших модулів)

data/ (директорія)
  └── Зберігає JSON файли:
      ├── contacts.json
      └── notes.json
```

---

## 📋 Опис основних модулів

### 🔌 Точка входу
- **main.py**: Основна програма з меню для взаємодії користувача

### 🏢 Сервіси (service/)
- **storage_service.py**: Управління завантаженням/збереженням даних у JSON
- **contact_book.py**: CRUD операції для контактів
- **note_book.py**: CRUD операції для нотаток

### 📦 Моделі (model/)
- **contact.py**: Клас Contact з валідацією телефону та email
- **note.py**: Клас Note з тегами та часом створення

### 🛠️ Утіліти (util/)
- **validation_util.py**: Валідація телефону та email через regex
- **date_util.py**: Функції для роботи з датами народження

### ⚠️ Виключення (exception/)
- **exceptions.py**: Користувацькі виключення та декоратор @input_error

---

## 📚 Залежності проекту

### Стандартні бібліотеки Python
- `datetime` - Робота з датами та часом
- `json` - Serialization даних
- `os` - Операції з файловою системою
- `re` - Регулярні вирази для валідації
- `pprint` - Форматований вивід (main.py)

### Залежності для розробки (опційно)
- `pytest>=7.0.0` - Тестування
- `pytest-cov>=4.0.0` - Покриття тестами
- `black>=22.0.0` - Форматування коду
- `flake8>=4.0.0` - Лінтер

