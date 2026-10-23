from validators import (
    check_mail,
    check_phone,
    normalize_fio,
    parse_line,
)

def test_valid_fio():
    fio, error = normalize_fio("иванов   иван")
    assert error is None
    assert fio == "Иванов Иван"

def test_invalid_fio():
    fio, error = normalize_fio("Иванов")
    assert fio is None
    assert error is not None

def test_valid_email():
    mail, error = check_mail("student@example.com")
    assert error is None
    assert mail == "student@example.com"

def test_invalid_email():
    mail, error = check_mail("bad-email")
    assert mail is None
    assert error is not None

def test_valid_phone():
    phone, error = check_phone("+79991234567")
    assert error is None
    assert phone == "79991234567"

def test_invalid_phone():
    phone, error = check_phone("123")
    assert phone is None
    assert error is not None

def test_valid_line():
    record, error = parse_line(
        "Иванов Иван;ivanov@example.com;+79991234567;09С41"
    )
    assert error is None
    assert record["fio"] == "Иванов Иван"
    assert record["group"] == "09с41"

def test_invalid_line():
    record, error = parse_line(
        "Иванов Иван;bad-email;123;09С41"
    )
    assert record is None
    assert error is not None

def test_empty_group():
    record, error = parse_line(
        "Иванов Иван;ivanov@example.com;+79991234567;"
    )
    assert record is None
    assert "группа" in error.lower()

def test_wrong_number_of_fields():
    record, error = parse_line("Иванов Иван;ivanov@example.com")
    assert record is None
    assert error is not None

