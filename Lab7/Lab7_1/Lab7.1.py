import json
from jsonschema import validate, ValidationError

# Загрузка данных и схемы
with open("schema.json", "r", encoding="utf-8") as schema_file:
    schema = json.load(schema_file)

with open("ex_1.json", "r", encoding="utf-8") as json_file:
    data1 = json.load(json_file)

with open("ex_1_with_error.json", "r", encoding="utf-8") as json_file:
    data2 = json.load(json_file)


# Функция валидации данных по схеме
def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("Файл прошел валидацию.")
    except ValidationError as e:
        print("Файл не прошел валидацию. Ошибка:")
        print(e)

# Запуск валидации
validate_json(data1, schema)
validate_json(data2, schema)