import json

# Загрузка исходного JSON файла
with open('ex_3.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Новый объект для добавления в массив invoices
new_invoice = {
    "id": 3,
    "total": 150.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 1,
            "price": 100.00
        },
        {
            "name": "item 5",
            "quantity": 1,
            "price": 50.00
        }
    ]
}

# Добавление нового объекта в массив invoices
data["invoices"].append(new_invoice)

# Сохранение изменений в новый файл ex_3_updated.json
with open('ex_3_updated.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print("Файл успешно обновлен и сохранен как ex_3_updated.json.")
