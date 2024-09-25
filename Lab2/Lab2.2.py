from PIL import Image
import sys
import numpy as np

#python Lab2\Lab2.2.py Lab2\img.jpg

# Получаем путь к изображению из системного параметра
if len(sys.argv) < 2:
    print("Укажите путь к изображению в качестве аргумента.")
    sys.exit(1)

image_path = sys.argv[1]

# Открытие изображения
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Файл {image_path} не найден.")
    sys.exit(1)

# Преобразование изображения в массив NumPy
image_array = np.array(image)

# Разделение изображения на каналы
r_channel = image_array[:, :, 0]  # Красный канал
g_channel = image_array[:, :, 1]  # Зеленый канал
b_channel = image_array[:, :, 2]  # Синий канал

# Подсчет сумм по каждому каналу
r_sum = np.sum(r_channel)
g_sum = np.sum(g_channel)
b_sum = np.sum(b_channel)

# Определение, какой канал больше
if r_sum > g_sum and r_sum > b_sum:
    dominant_color = 'Красный (R)'
elif g_sum > r_sum and g_sum > b_sum:
    dominant_color = 'Зеленый (G)'
else:
    dominant_color = 'Синий (B)'

# Вывод результата
print(f"Больше всего используется: {dominant_color}")
print(f"Суммы каналов - R: {r_sum}, G: {g_sum}, B: {b_sum}")
