from pathlib import Path
import argparse

def check_files_in_directory(dirpath, files):
    dirpath = Path(dirpath)  # Преобразуем строку в Path объект
    present_files = []
    absent_files = []

    for file in files:
        file_path = dirpath / file  # Объединяем путь с именем файла
        if file_path.is_file():
            present_files.append(file)
        else:
            absent_files.append(file)

    # Вывод списков на экран
    print("Файлы, присутствующие в папке:")
    for file in present_files:
        print(file)

    print("\nФайлы, отсутствующие в папке:")
    for file in absent_files:
        print(file)

    # Запись списков в файлы
    with open("present_files.txt", "w") as present_file:
        for file in present_files:
            present_file.write(file + "\n")

    with open("absent_files.txt", "w") as absent_file:
        for file in absent_files:
            absent_file.write(file + "\n")


def directory_info(dirpath):
    dirpath = Path(dirpath)
    total_size = 0
    total_files = 0

    for item in dirpath.iterdir():
        if item.is_file():
            total_files += 1
            total_size += item.stat().st_size

    print(f"Количество файлов в папке: {total_files}")
    print(f"Общий размер файлов: {total_size} байт")


def main():
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Проверка наличия файлов в директории")
    parser.add_argument('--dirpath', type=str, default=Path.cwd(), help="Путь к папке (по умолчанию текущая)")
    parser.add_argument('--files', nargs='*', help="Список файлов для проверки")

    args = parser.parse_args()

    if args.files:
        # Проверка файлов в указанной директории
        check_files_in_directory(args.dirpath, args.files)
    else:
        # Вывод общей информации о папке, если файлы не переданы
        directory_info(args.dirpath)


if __name__ == "__main__":
    main()
