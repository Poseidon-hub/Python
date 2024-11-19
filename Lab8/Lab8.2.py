from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# Создаем базовый класс для моделей
Base = declarative_base()

# Модель для таблицы Транспорт
class Transport(Base):
    __tablename__ = 'Транспорт'
    Номер_машины = Column(Integer, primary_key=True)
    Марка = Column(String)
    Дата_регистрации = Column(Date)
    Цвет = Column(String)

# Модель для таблицы Отправитель
class Отправитель(Base):
    __tablename__ = "Отправитель"
    Код_отправителя = Column(Integer, primary_key=True, autoincrement=True)
    Фамилия = Column(String)
    Имя = Column(String)
    Отчество = Column(String)
    Дата_рождения = Column(Date)
    Индекс = Column(String)
    Город = Column(String)
    Улица = Column(String)
    Дом = Column(String)
    Квартира = Column(String)
    Телефон = Column(String)

class Получатель(Base):
    __tablename__ = "Получатель"
    Код_получателя = Column(Integer, primary_key=True, autoincrement=True)
    Фамилия = Column(String)
    Имя = Column(String)
    Отчество = Column(String)
    Дата_рождения = Column(Date)
    Индекс = Column(String)
    Город = Column(String)
    Улица = Column(String)
    Дом = Column(String)
    Квартира = Column(String)
    Телефон = Column(String)

# Создаем подключение к базе данных и таблицы
engine = create_engine('sqlite:///delivery_service.db')
Base.metadata.create_all(engine)

# Создаем сессию для работы с данными
Session = sessionmaker(bind=engine)
session = Session()

session.query(Transport).delete()
session.commit()

# Добавление данных в таблицу Транспорт
new_transport = Transport(
    Номер_машины=1,
    Марка='BMW',
    Дата_регистрации=date(2022, 1, 1),  # Конвертируем дату в объект date
    Цвет='Черный'
)
new_transport = Transport(
    Номер_машины=2,
    Марка='BMW',
    Дата_регистрации=date(2022, 1, 1),  # Конвертируем дату в объект date
    Цвет='Черный'
)
session.add(new_transport)

# Добавление данных в таблицу Отправитель
new_sender = Отправитель(
    Фамилия="Иванов",
    Имя="Иван",
    Отчество="Иванович",
    Дата_рождения=date(1990, 5, 20),
    Индекс="123456",
    Город="Москва",
    Улица="Ленина",
    Дом="10",
    Квартира="5",
    Телефон="1234567890"
)
new_sender = Отправитель(
    Фамилия="Петров",
    Имя="Иван",
    Отчество="Иванович",
    Дата_рождения=date(1990, 5, 20),
    Индекс="123456",
    Город="Москва",
    Улица="Ленина",
    Дом="10",
    Квартира="5",
    Телефон="1234567890"
)

# Добавление данных в таблицу Получатель
new_receiver = Получатель(
    Фамилия="Петров",
    Имя="Петр",
    Отчество="Петрович",
    Дата_рождения=date(1985, 3, 15),
    Индекс="654321",
    Город="Санкт-Петербург",
    Улица="Куйбышева",
    Дом="20",
    Квартира="15",
    Телефон="0987654321"
)
new_receiver = Получатель(
    Фамилия="Иванов",
    Имя="Петр",
    Отчество="Петрович",
    Дата_рождения=date(1985, 3, 15),
    Индекс="654321",
    Город="Санкт-Петербург",
    Улица="Куйбышева",
    Дом="20",
    Квартира="15",
    Телефон="0987654321"
)

# Сохранение данных в базе
session.add(new_sender)
session.add(new_receiver)

# Сохраняем изменения
session.commit()

# Закрываем сессию
session.close()