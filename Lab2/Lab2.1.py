from PIL import Image
import matplotlib.pyplot as plt

# Открытие изображения
image = Image.open('img.jpg')

# Разделение на каналы RGB
r, g, b = image.split()

# Настройка окна для отображения изображений с высоким DPI
fig, axs = plt.subplots(1, 4, figsize=(15, 4), dpi=600)

# Отображение исходного изображения
axs[0].imshow(image)
axs[0].set_title('Исходное изображение')
axs[0].axis('off')

# Отображение канала R (красный)
axs[1].imshow(r, cmap='Reds')
axs[1].set_title('Канал R')
axs[1].axis('off')

# Отображение канала G (зелёный)
axs[2].imshow(g, cmap='Greens')
axs[2].set_title('Канал G')
axs[2].axis('off')

# Отображение канала B (синий)
axs[3].imshow(b, cmap='Blues')
axs[3].set_title('Канал B')
axs[3].axis('off')

# Показать изображения
plt.show()
