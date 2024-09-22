from pathlib import Path


def create_missing_files():
    # Директория, в которой хранится absent_files.txt и где нужно создавать файлы
    target_dir = Path("C:/Users/matve/PythonData/pythonProject")

    # Путь к файлу absent_files.txt
    absent_files_path = target_dir / "absent_files.txt"

    # Проверка, существует ли файл absent_files.txt
    if not absent_files_path.exists():
        print(f"Файл {absent_files_path} не найден!")
        return

    # Чтение списка отсутствующих файлов
    absent_files = []
    with absent_files_path.open("r") as file:
        absent_files = file.read().splitlines()

    # Создание отсутствующих файлов в директории target_dir
    for filename in absent_files:
        file_path = target_dir / filename
        try:
            file_path.touch(exist_ok=True)  # Создание файла
            print(f"Создан файл: {file_path}")
        except Exception as e:
            print(f"Ошибка при создании файла {file_path}: {e}")


def main():
    # Создание отсутствующих файлов в target_dir
    create_missing_files()


if __name__ == "__main__":
    main()
