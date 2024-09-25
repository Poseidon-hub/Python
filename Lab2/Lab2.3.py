from PIL import Image, ImageDraw, ImageFont

# Открытие исходного изображения с правильным путем
image = Image.open(r'Lab2\img.jpg')

# Создание объекта для рисования на изображении
draw = ImageDraw.Draw(image)

# Установка текста для водяного знака
text = "Водяной знак текст"
font_size = 170

# Загрузка шрифта для текста
font = ImageFont.load_default()

# Открытие изображения, которое будет водяным знаком
watermark = Image.open(r'Lab2\watermark.png').convert("RGBA")

# Изменение размера водяного знака
scale_factor = 1
watermark_width, watermark_height = watermark.size
new_width = int(watermark_width * scale_factor)
new_height = int(watermark_height * scale_factor)
watermark = watermark.resize((new_width, new_height), Image.LANCZOS)  # Сохраняем пропорции

# Определение положения водяного знака (нижний правый угол)
watermark_position = (image.width - new_width - 10, image.height - new_height)  # Положение водяного знака

# Наложение водяного знака на изображение
image.paste(watermark, watermark_position, watermark)

# Определение положения текста водяного знака (правее знака)
text_position = (watermark_position[0] - 1700, watermark_position[1] + 150)  # Положение текста

# Добавление текста на изображение с прозрачностью
draw.text(text_position, text, font=font, fill=(255, 255, 255, 128))  # Белый цвет с прозрачностью 128

# Сохранение изображения с водяным знаком в формате JPG
image.save(r'Lab2\image_with_watermark.jpg', 'JPEG')

# Показать результат
image.show()

#python Lab2\Lab2.3.py