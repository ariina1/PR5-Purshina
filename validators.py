
import re

def normalize_fio(value):
    """Нормализует ФИО и проверяет количество слов."""
    words = value.split()
    if len(words) < 2:
        return None, "В ФИО меньше двух слов"
    if not all(re.fullmatch(r"[А-ЯЁа-яёA-Za-z-]+", word) for word in words):
        return None, "ФИО содержит недопустимые символы"
    fio = " ".join(word.capitalize() for word in words)
    return fio, None

def check_mail(value):
    """Проверяет адрес электронной почты."""
    mail = value.strip().lower()

    if mail.count("@") != 1:
        return None, f"Почта неверная: {value.strip()}"
    local, domain = mail.split("@")
    if not local or not domain or "." not in domain:
        return None, f"Почта неверная: {value.strip()}"
    if domain.startswith(".") or domain.endswith("."):
        return None, f"Почта неверная: {value.strip()}"
    if any(ch.isspace() for ch in mail):
        return None, f"Почта неверная: {value.strip()}"
    return mail, None

def check_phone(value):
    """Проверяет телефон и приводит его к формату из 11 цифр."""
    digits = "".join(ch for ch in value if ch.isdigit())
    if len(digits) != 11 or digits[0] not in "78":
        return None, f"Телефон неверный: {value.strip()}"
    if digits[0] == "8":
        digits = "7" + digits[1:]

    return digits, None

def parse_line(line):
    """Проверяет одну строку с четырьмя полями анкеты."""
    fields = line.split(";")
    if len(fields) != 4:
        return None, f"Полей должно быть 4, получено {len(fields)}"
    fio, mail, phone, group = (
        field.strip() for field in fields
    )
    fio, error = normalize_fio(fio)
    if error:
        return None, error
    mail, error = check_mail(mail)
    if error:
        return None, error
    phone, error = check_phone(phone)
    if error:
        return None, error
    group = "".join(group.split()).lower()
    if not group:
        return None, "Группа пустая"
    record = {
        "fio": fio,
        "mail": mail,
        "phone": phone,
        "group": group,
    }
    return record, None

def mask_phone(phone):
    """Маскирует телефон для вывода на экран."""
    return f"+7 ({phone[1:4]}) ***-**-{phone[-2:]}"

