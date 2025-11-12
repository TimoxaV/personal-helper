# Структура імпортів проекту

## 📊 Граф залежностей між модулями

```
test.py (ТОЧКА ВХОДУ)
  ├── import model.Contacts_save_and_finding
  │   └── ContactBook class
  ├── import util.validation_util
  │   └── ValidationUtil class
  └── import exception.exceptions
      ├── ContactNotFoundException
      ├── WrongEmailFormatException
      └── WrongPhoneNumberFormatException

model/Contacts_save_and_finding.py
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

## 📝 Детальна таблиця імпортів

### test.py
```python
import sys                                    # stdlib
import os                                     # stdlib
from datetime import datetime, timedelta      # stdlib
from pathlib import Path                      # stdlib

from model.Contacts_save_and_finding import ContactBook
from util.validation_util import ValidationUtil
from exception.exceptions import (
    ContactNotFoundException,
    WrongEmailFormatException,
    WrongPhoneNumberFormatException
)
```

### model/Contacts_save_and_finding.py
```python
import sys                                    # stdlib
import os                                     # stdlib
import pickle                                 # stdlib
from datetime import datetime                 # stdlib
from pathlib import Path                      # stdlib

from util.validation_util import ValidationUtil
from exception.exceptions import (
    ContactNotFoundException,
    WrongEmailFormatException,
    WrongPhoneNumberFormatException
)
from model.contact import Contact
```

### model/contact.py
```python
import sys                                    # stdlib
import os                                     # stdlib
from datetime import datetime                 # stdlib
from pathlib import Path                      # stdlib

from exception.exceptions import (
    input_error,
    WrongEmailFormatException,
    WrongPhoneNumberFormatException
)
from util.validation_util import ValidationUtil
```

### util/validation_util.py
```python
import re                                     # stdlib
# нема залежностей від своїх модулів
```

### exception/exceptions.py
```python
# нема імпортів
```

---

## 🔄 Порядок завантаження модулів

```
1. exception/exceptions.py                    (базовий - нема залежностей)
   ↓
2. util/validation_util.py                    (залежить тільки від stdlib)
   ↓
3. model/contact.py                           (залежить від exception + util)
   ↓
4. model/Contacts_save_and_finding.py         (залежить від contact + exception + util)
   ↓
5. test.py                                    (залежить від усього)
```

---

## ✅ Циркулярні залежності

✅ **НЕМАЄ циркулярних залежностей** - добра архітектура!

```
exception ← використовується усім
util ← використовується всіма моделями
contact ← використовується ContactBook
ContactBook ← використовується тестами
test ← точка входу
```

---

## 📌 Чистота імпортів

| Файл | Залежності | Статус |
|------|-----------|--------|
| exception/exceptions.py | 0 | ✅ Чистий |
| util/validation_util.py | 1 (re) | ✅ Чистий |
| model/contact.py | 3 (exception, util, stdlib) | ✅ Нормально |
| model/Contacts_save_and_finding.py | 4 (contact, exception, util, stdlib) | ✅ Нормально |
| test.py | 5 (всі модулі) | ✅ Тестовий файл |

---

## 🎯 Рекомендації

1. **Не змінювати** порядок依賴 - архітектура оптимальна ✅
2. **Не додавати** циркулярні імпорти ❌
3. **Завжди** встанови `__init__.py` у папках 📁
4. **Використовуй** відносні імпорти у пакетах 📦
