import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from skimage.exposure import histogram

# Загрузка изображения с помощью Pillow
image_path = 'img.jpg'
image = Image.open(image_path)

# Преобразование изображения в массив numpy
image_np = np.array(image)

# Создание подграфиков: 4 строки и 2 колонки
fig, axes = plt.subplots(4, 2, figsize=(12, 10))

# Показать исходное изображение
axes[0, 0].axis('off')
axes[1, 0].imshow(image)
axes[1, 0].set_title('Исходное изображение')

# Получение общей гистограммы изображения с помощью PIL
histogram_values = image.histogram()

# Построение общей гистограммы
axes[0, 1].hist(histogram_values, bins=256, color='gray', alpha=0.6)
axes[0, 1].set_title('Гистограмма изображения')

# Получение и вывод гистограмм для каждого цветового канала
colors = ['Red', 'Green', 'Blue']
for i, color in enumerate(colors):
    channel = image_np[:, :, i]

    # Нормализуем значения пикселей
    channel_float = channel / 255.0

    # Получаем гистограмму для каждого канала
    hist, hist_centers = histogram(channel_float)

    # Отображаем гистограмму для каждого канала в соответствующих строках второй колонки
    axes[i + 1, 1].plot(hist_centers, hist, color=color.lower())
    axes[i + 1, 1].set_title(f'Гистограмма {color} канала')

    # Убираем пустую область в первой колонке для гистограмм
    axes[i + 1, 0].axis('off')

# Настройка макета
plt.tight_layout()
plt.show()
