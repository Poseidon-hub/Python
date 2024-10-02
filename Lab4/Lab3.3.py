import cv2

# Указываем путь к видеофайлу
video_path = 'Iceland.mp4'

# Открываем видеоклип
cap = cv2.VideoCapture(video_path)

# Проверяем, открылся ли видеоклип
if not cap.isOpened():
    print(f"Не удалось открыть файл {video_path}")
    exit()

# Получаем параметры видео
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Отображаем имя файла и FPS на каждом кадре
    text = f"File: {video_path}, FPS: {fps}"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Показываем текущий кадр
    cv2.imshow('Video', frame)

    # Останавливаем по нажатию клавиши 'q'
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
