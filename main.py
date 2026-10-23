
from validators import parse_line
from storage import read_lines, write_results
from report import print_report

def main():
    try:
        lines = read_lines()
    except FileNotFoundError as error:
        print(f"Ошибка: {error}")
        return
    accepted = []
    rejected = []
    for number, line in enumerate(lines, 1):
        line = line.rstrip("\r\n")

        if not line.strip():
            continue
        record, error = parse_line(line)
        if error:
            rejected.append({
                "number": number,
                "line": line,
                "reason": error,
            })
        else:
            accepted.append(record)
    accepted.sort(key=lambda item: item["fio"].casefold())
    write_results(accepted, rejected)
    print_report(accepted, rejected, len(lines))
    print("\nРезультаты сохранены в ok.txt и errors.txt.")
if __name__ == "__main__":
    main()

