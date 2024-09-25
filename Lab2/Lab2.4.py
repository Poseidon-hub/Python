from PIL import Image, ImageDraw, ImageFont

# Функция для создания карточки
def create_card(number):
    # Создание пустого изображения с белым фоном
    card = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(card)

    # Рисуем синюю рамку
    border_color = (0, 0, 255)  # Синий цвет
    border_thickness = 5
    draw.rectangle(
        [(0, 0), (100, 100)],
        outline=border_color,
        width=border_thickness
    )

    # Установка шрифта для цифр
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    # Определение текста для карточки
    text = str(number)

    # Вычисляем размер текста и его положение
    text_bbox = draw.textbbox((0, 0), text, font=font)  # Новый метод textbbox
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_position = ((100 - text_width) // 2, (100 - text_height) // 2)

    # Рисуем текст на карточке
    text_color = (255, 0, 0)  # Красный цвет
    draw.text(text_position, text, fill=text_color, font=font)

    return card

# Создание и сохранение карточек
for i in range(1, 4):
    card_image = create_card(i)
    card_image.save(f'card_{i}.png', 'PNG')  # Сохранение карточки
    card_image.show()  # Показать карточку
