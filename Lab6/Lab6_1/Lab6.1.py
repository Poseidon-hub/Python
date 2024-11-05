import xmlschema
from lxml import etree

# Путь к XML и XSD файлам
xml_file = 'ex_1.xml'
invalid_xml_file = 'ex_1_invalid.xml'
xsd_file = 'ex_1.xsd'

# Загружаем схему XSD
schema = xmlschema.XMLSchema(xsd_file)

# Функция для проверки валидации XML файла
def validate_xml(file_path, schema):
    try:
        schema.validate(file_path)
        print(f"Файл {file_path} прошел валидацию")
    except xmlschema.XMLSchemaValidationError as e:
        print(f"Ошибка валидации в файле {file_path}:", e)

# Проверка валидации исходного и неверного XML файлов
validate_xml(xml_file, schema)
validate_xml(invalid_xml_file, schema)
