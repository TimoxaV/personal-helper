import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# Додаємо батьківську папку до path для імпортів
sys.path.insert(0, str(Path(__file__).parent))

from model.Contacts_save_and_finding import ContactBook
from util.validation_util import ValidationUtil
from exception.exceptions import (
    ContactNotFoundException,
    WrongEmailFormatException,
    WrongPhoneNumberFormatException
)


def test_add_contacts():
    """Тест додавання контактів"""
    print("=" * 60)
    print("📝 ТЕСТ 1: Додавання контактів")
    print("=" * 60)
    
    book = ContactBook()
    
    # Додавання валідних контактів
    result1 = book.add_contact(
        "John Doe",
        "+380501234567",
        "john@example.com",
        "Kyiv, Ukraine",
        "1990-05-15"
    )
    print(f"✅ {result1}")
    
    result2 = book.add_contact(
        "Jane Smith",
        "+380951234567",
        "jane@example.com",
        "Lviv, Ukraine",
        "1995-12-20"
    )
    print(f"✅ {result2}")
    
    result3 = book.add_contact(
        "Bob Wilson",
        "+380661234567",
        "bob@example.com",
        "Odesa, Ukraine",
        "1988-03-10"
    )
    print(f"✅ {result3}")
    
    # Спроба додати дублікат
    try:
        book.add_contact(
            "John Doe",
            "+380501111111",
            "john2@example.com",
            "Kyiv",
            "1990-05-15"
        )
    except ContactNotFoundException as e:
        print(f"❌ Помилка: {e}")
    
    # Тест невалідного телефону
    try:
        book.add_contact(
            "Invalid Phone",
            "123",
            "invalid@example.com",
            "Kyiv",
            "2000-01-01"
        )
    except WrongPhoneNumberFormatException as e:
        print(f"❌ Помилка телефону: {e}")
    
    # Тест невалідного email
    try:
        book.add_contact(
            "Invalid Email",
            "+380501234567",
            "invalid-email",
            "Kyiv",
            "2000-01-01"
        )
    except WrongEmailFormatException as e:
        print(f"❌ Помилка email: {e}")
    
    print()
    return book


def test_validation():
    """Тест валідації телефону та email"""
    print("=" * 60)
    print("✔️ ТЕСТ 2: Валідація телефону та email")
    print("=" * 60)
    
    # Тестування телефону
    valid_phones = ["+380501234567", "+1234567890", "0501234567"]
    invalid_phones = ["123", "abc", ""]
    
    print("📞 Валідація телефонів:")
    for phone in valid_phones:
        result = ValidationUtil.validate_phone(phone)
        print(f"  ✅ '{phone}': {bool(result)}")
    
    for phone in invalid_phones:
        result = ValidationUtil.validate_phone(phone)
        print(f"  ❌ '{phone}': {bool(result)}")
    
    # Тестування email
    valid_emails = ["john@example.com", "test@mail.co.uk", "user+tag@domain.org"]
    invalid_emails = ["invalid-email", "@example.com", "user@", ""]
    
    print("\n📧 Валідація email:")
    for email in valid_emails:
        result = ValidationUtil.validate_email(email)
        print(f"  ✅ '{email}': {bool(result)}")
    
    for email in invalid_emails:
        result = ValidationUtil.validate_email(email)
        print(f"  ❌ '{email}': {bool(result)}")
    
    print()


def test_search_contacts(book):
    """Тест пошуку контактів"""
    print("=" * 60)
    print("🔍 ТЕСТ 3: Пошук контактів")
    print("=" * 60)
    
    keywords = ["John", "example.com", "+380501234567", "Kyiv"]
    
    for keyword in keywords:
        results = book.search_contacts(keyword)
        print(f"\n🔎 Пошук за '{keyword}':")
        if results:
            for contact in results:
                print(f"  ✅ Знайдено: {contact.name} - {contact.email}")
        else:
            print(f"  ❌ Контакти не знайдені")
    
    print()


def test_edit_contact(book):
    """Тест редагування контактів"""
    print("=" * 60)
    print("✏️ ТЕСТ 4: Редагування контактів")
    print("=" * 60)
    
    result = book.edit_contact(
        "John Doe",
        phone="+380501999999",
        email="john.new@example.com"
    )
    print(f"✅ {result}")
    
    contact = book.get_contact("John Doe")
    print(f"   Новий телефон: {contact.phone}")
    print(f"   Новий email: {contact.email}")
    
    try:
        book.edit_contact("Non Existent", phone="+380501234567")
    except ContactNotFoundException as e:
        print(f"❌ Помилка: {e}")
    
    print()


def test_birthdays_in_days(book):
    """Тест виведення днів народження"""
    print("=" * 60)
    print("🎂 ТЕСТ 5: Дні народження через N днів")
    print("=" * 60)
    
    today = datetime.today()
    
    print(f"\n📋 Усі контакти на {today.date()}:\n")
    for contact in book.get_all_contacts():
        next_birthday = contact.birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        
        days_until = (next_birthday - today).days
        print(f"  👤 {contact.name}")
        print(f"     День народження: {contact.birthday.date()}")
        print(f"     Наступний день: {next_birthday.date()}")
        print(f"     Днів до дня: {days_until}\n")
    
    print()


def test_save_and_load(book):
    """Тест збереження та завантаження"""
    print("=" * 60)
    print("💾 ТЕСТ 6: Збереження та завантаження контактів")
    print("=" * 60)
    
    save_result = book.save("test_contacts.pkl")
    print(f"✅ {save_result}")
    
    new_book = ContactBook()
    load_result = new_book.load("test_contacts.pkl")
    print(f"✅ {load_result}")
    
    print(f"\n📊 Завантажено контактів: {len(new_book.get_all_contacts())}")
    for contact in new_book.get_all_contacts():
        print(f"  ✅ {contact.name} - {contact.email}")
    
    if os.path.exists("test_contacts.pkl"):
        os.remove("test_contacts.pkl")
        print("\n🗑️ Тестовий файл видалено")
    
    print()


def test_delete_contact(book):
    """Тест видалення контактів"""
    print("=" * 60)
    print("🗑️ ТЕСТ 7: Видалення контактів")
    print("=" * 60)
    
    print(f"Контактів до видалення: {len(book.get_all_contacts())}")
    
    result = book.delete_contact("Bob Wilson")
    print(f"✅ {result}")
    
    print(f"Контактів після видалення: {len(book.get_all_contacts())}")
    
    try:
        book.delete_contact("Non Existent")
    except ContactNotFoundException as e:
        print(f"❌ Помилка: {e}")
    
    print()


def test_display_all_contacts(book):
    """Тест виведення всіх контактів"""
    print("=" * 60)
    print("📋 ТЕСТ 8: Вивід всіх контактів")
    print("=" * 60)
    print(book)
    print()


if __name__ == "__main__":
    print("\n" + "🚀" * 30)
    print("ТЕСТУВАННЯ КНИГИ КОНТАКТІВ")
    print("🚀" * 30 + "\n")
    
    test_validation()
    book = test_add_contacts()
    test_search_contacts(book)
    test_edit_contact(book)
    test_birthdays_in_days(book)
    test_display_all_contacts(book)
    test_save_and_load(book)
    test_delete_contact(book)
    
    print("=" * 60)
    print("✅ ВСІ ТЕСТИ ЗАВЕРШЕНІ")
    print("=" * 60)