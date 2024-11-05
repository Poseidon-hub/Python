import xml.etree.ElementTree as ET

# Функция для добавления отступов в XML
def indent(elem, level=0):
    i = "\n" + level * "    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for child in elem:
            indent(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# Загрузка исходного XML файла
file_path = "ex_2.xml"
tree = ET.parse(file_path)
root = tree.getroot()

# Добавление нового элемента Item
new_item = ET.Element("Item")
ET.SubElement(new_item, "ArtName").text = "Сыр Пармезан"
ET.SubElement(new_item, "Barcode").text = "2000000000150"
ET.SubElement(new_item, "QNT").text = "100,75"
ET.SubElement(new_item, "QNTPack").text = "100,75"
ET.SubElement(new_item, "Unit").text = "шт"
ET.SubElement(new_item, "SN1").text = "00000015"
ET.SubElement(new_item, "SN2").text = "10.04.2020"
ET.SubElement(new_item, "QNTRows").text = "10"

# Добавляем новый элемент в секцию Detail
detail_section = root.find("Detail")
detail_section.append(new_item)

# Пересчитываем Summ и SummRows
total_quantity = sum(float(item.find("QNT").text.replace(',', '.')) for item in detail_section.findall("Item"))
total_rows = sum(int(item.find("QNTRows").text) for item in detail_section.findall("Item"))

# Обновляем значения в Summary
summary = root.find("Summary")
summary.find("Summ").text = f"{total_quantity:.2f}".replace('.', ',')
summary.find("SummRows").text = str(total_rows)

# Применяем отступы
indent(root)

# Сохраняем обновленный файл
new_file_path = "ex_2_modified.xml"
tree.write(new_file_path, encoding="UTF-8", xml_declaration=True)

print("Файл успешно обновлен и сохранен с форматированием.")
