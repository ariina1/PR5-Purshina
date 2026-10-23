from collections import Counter
from validators import mask_phone

def show_table(accepted):
    """Выводит корректные анкеты в виде таблицы."""
    print("\n=== КОРРЕКТНЫЕ АНКЕТЫ ===")
    print(
        f"{'№':>3} {'ФИО':<28} {'Почта':<25} "
        f"{'Телефон':<19} Группа"
    )
    print("-" * 88)
    for number, item in enumerate(accepted, 1):
        print(
            f"{number:>3} "
            f"{item['fio'][:28]:<28} "
            f"{item['mail'][:25]:<25} "
            f"{mask_phone(item['phone']):<19} "
            f"{item['group']}"
        )
    print("-" * 88)

def print_report(accepted, rejected, total_lines):
    """Выводит итоговые результаты обработки."""
    show_table(accepted)
    print(f"\nОтклонено строк: {len(rejected)}")
    for item in rejected:
        print(
            f"Строка {item['number']}: {item['reason']}"
        )
        print(f"  Исходная строка: {item['line']}")

    print(f"\nВсего строк в файле: {total_lines}")
    print(f"Принято: {len(accepted)} | Отклонено: {len(rejected)}")
    print("\nПо группам:")
    groups = Counter(item["group"] for item in accepted)
    if groups:
        for group, count in sorted(groups.items()):
            print(f"  {group:<8} {count}")
    else:
        print("  Корректных анкет нет.")
