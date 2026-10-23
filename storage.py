from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "anketa.txt"
OK_FILE = BASE_DIR / "ok.txt"
ERROR_FILE = BASE_DIR / "errors.txt"

ef read_lines():
    """Читает строки из файла с анкетами."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Файл {INPUT_FILE.name} не найден")

    with INPUT_FILE.open("r", encoding="utf-8") as file:
        return file.readlines()

def write_results(accepted, rejected):
    """Сохраняет корректные анкеты и ошибки в разные файлы."""
    with OK_FILE.open("w", encoding="utf-8") as file:
        for item in accepted:
            file.write(
                f"{item['fio']};{item['mail']};"
                f"{item['phone']};{item['group']}\n"
            )

    with ERROR_FILE.open("w", encoding="utf-8") as file:
        for item in rejected:
            file.write(
                f"Строка {item['number']}: {item['reason']} | "
                f"{item['line']}\n"
            )

