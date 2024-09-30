import os
import sys
import numpy as np
from skimage import io, transform, util, exposure
import random


# Атомарные преобразования
def rotate_image(image, angle=45):
    return transform.rotate(image, angle)


def flip_image(image):
    return np.fliplr(image)


def add_noise(image):
    return util.random_noise(image)


def adjust_brightness(image, gain=1.5):
    return exposure.adjust_gamma(image, gain)


def crop_image(image, crop_fraction=0.2):
    h, w = image.shape[:2]
    crop_h, crop_w = int(h * crop_fraction), int(w * crop_fraction)
    return image[crop_h:h - crop_h, crop_w:w - crop_w]


# Комплексное преобразование
def complex_transform(image):
    image = rotate_image(image, angle=random.randint(30, 60))
    image = flip_image(image)
    image = add_noise(image)
    return image


# Словарь преобразований
transformations = {
    'rotate': rotate_image,
    'flip': flip_image,
    'noise': add_noise,
    'brightness': adjust_brightness,
    'crop': crop_image,
    'complex': complex_transform
}


# Основная функция для обработки данных
def augment_images(input_folder, chosen_transformations):
    # Получаем список файлов изображений
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # Отслеживаем текущий номер файла (начинаем с 20, так как первые 20 — оригиналы)
    file_index = 20

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = io.imread(image_path)

        # Применяем выбранные пользователем преобразования
        for transformation in chosen_transformations:
            transformed_image = transformations[transformation](image)

            # Создаём новое имя файла с нумерацией, начиная с 0020
            new_image_name = f"{file_index:04}.jpg"  # Пронумеровываем изображения с ведущими нулями (4 цифры)
            new_image_path = os.path.join(input_folder, new_image_name)

            # Сохраняем преобразованное изображение
            io.imsave(new_image_path, (transformed_image * 255).astype(np.uint8))

            # Увеличиваем индекс для следующего файла
            file_index += 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python augment.py <path_to_images_folder> <transformations>")
        sys.exit(1)

    # Путь к папке с изображениями
    input_folder = sys.argv[1]

    # Выбранные преобразования пользователем
    chosen_transformations = sys.argv[2:]

    # Запускаем процесс аугментации
    augment_images(input_folder, chosen_transformations)


# python Lab3\Lab3.1.py Lab3\plates\train\dirty complex
# Папку plates заархивировал
