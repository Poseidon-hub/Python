from moviepy.editor import VideoFileClip
from skimage.transform import resize
import os
import numpy as np
from PIL import Image


def extract_frames(video_path, start_time, end_time, output_folder, frame_step=10):
    # Открываем видеоклип
    clip = VideoFileClip(video_path).subclip(start_time, end_time)

    # Проверяем, существует ли папка для сохранения кадров, если нет - создаем
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_number = 0  # Для именования кадров

    # Пробегаемся по всем кадрам в клипе с шагом
    for t in range(0, int(clip.duration * clip.fps), frame_step):
        # Получаем кадр в виде numpy массива
        frame = clip.get_frame(t / clip.fps)

        # Преобразуем кадр для изменения размера
        aspect_ratio = frame.shape[1] / frame.shape[0]
        new_height = int(250 / aspect_ratio)

        # Изменяем размер изображения до 250px по ширине, сохраняя соотношение сторон
        frame_resized = resize(frame, (new_height, 250), anti_aliasing=True)

        # Преобразуем массив в изображение и сохраняем
        frame_image = Image.fromarray((frame_resized * 255).astype(np.uint8))
        frame_filename = os.path.join(output_folder, f"{frame_number}.png")
        frame_image.save(frame_filename)

        frame_number += 1

    clip.close()
    print(f"Извлечение кадров завершено. Кадры сохранены в папке: {output_folder}")


# Пример вызова функции
video_path = 'Iceland.mp4'
start_time = 10  # Начало в секундах
end_time = 30  # Конец в секундах
output_folder = 'img'
frame_step = 10  # Шаг извлечения кадров

extract_frames(video_path, start_time, end_time, output_folder, frame_step)
