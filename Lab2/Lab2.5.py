import os
from PIL import Image

# Функция для создания эскизов
def create_thumbnails(directory, extension):
    # Получаем все файлы с указанным расширением
    files = [f for f in os.listdir(directory) if f.endswith(extension)]

    if not files:
        print(f"Нет файлов с расширением {extension} в директории {directory}")
        return

    for file in files:
        # Открываем изображение
        image_path = os.path.join(directory, file)
        with Image.open(image_path) as img:
            # Создаем эскиз (thumbnail) размером 50x50
            img.thumbnail((50, 50))

            # Выводим эскиз на экран
            img.show()

# Основная программа
if __name__ == "__main__":
    directory = os.getcwd()
    # Расширение файлов, которые нужно найти
    extension = input("Введите расширение файла (например, '.jpg'): ")

    # Создаем эскизы и выводим их на экран
    create_thumbnails(directory, extension)
