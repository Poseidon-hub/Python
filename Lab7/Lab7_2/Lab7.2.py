import json

# Открываем и читаем содержимое файла ex_2.json
with open('ex_2.json', 'r') as file:
    # Парсим JSON-данные
    data = json.loads('[' + file.read() + ']')  # Добавляем скобки, чтобы привести к правильному формату

# Извлекаем имена и номера телефонов
users_dict = {user["name"]: user["phoneNumber"] for user in data}

# Выводим результат
print(users_dict)

# Сохраняем отформатированные данные в новый файл
with open('formatted_ex_2.json', 'w') as formatted_file:
    json.dump(data, formatted_file, indent=4)
