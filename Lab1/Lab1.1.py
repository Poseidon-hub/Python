from pathlib import Path
import shutil
import sys

def find_and_copy_small_files(directory):
    # Если директория не указана, используем текущую
    if directory is None:
        directory = Path.cwd()
    else:
        directory = Path(directory)

    # Проверяем, существует ли директория
    if not directory.is_dir():
        print(f"Указанная директория не существует: {directory}")
        return

    small_files = []

    # Проходим по всем файлам в директории
    for file_path in directory.rglob('*'):  # Ищем все файлы в поддиректориях
        if file_path.is_file() and file_path.stat().st_size < 2048:  # Проверка размера файла
            small_files.append(file_path)

    # Выводим список маленьких файлов
    if small_files:
        print("Найденные маленькие файлы:")
        for file in small_files:
            print(file)
    else:
        print("Маленькие файлы не найдены.")
        return

    # Создаем папку 'small' если её нет
    small_folder = directory / 'small'
    small_folder.mkdir(exist_ok=True)

    # Копируем маленькие файлы в папку 'small'
    for file in small_files:
        shutil.copy(file, small_folder)

    print(f"Маленькие файлы скопированы в папку: {small_folder}")

if __name__ == "__main__":
    # Путь к директории передается в качестве аргумента командной строки
    directory = sys.argv[1] if len(sys.argv) > 1 else None
    find_and_copy_small_files(directory)
