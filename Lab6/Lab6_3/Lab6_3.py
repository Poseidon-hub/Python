import xml.etree.ElementTree as ET

# Загрузка XML файла
file_path = "ex_3.xml"
tree = ET.parse(file_path)
root = tree.getroot()

# Поиск и вывод данных о товарах
print("Товары в счет-фактуре:")
for item in root.findall(".//СведТов"):
    name = item.get("НаимТов")
    quantity = item.get("КолТов")
    price = item.get("ЦенаТов")
    print(f"Наименование: {name}, Количество: {quantity}, Цена за единицу: {price}")
