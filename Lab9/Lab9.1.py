from openpyxl import Workbook

# Исходные данные
data = {
    "Бухгалтерия": [
        {"Таб. номер": "0002", "Фамилия": "Петров П.П.", "Оклад": 3913.04, "Надбавки": 2608.70},
        {"Таб. номер": "0005", "Фамилия": "Васин В.В.", "Оклад": 5934.78, "Надбавки": 913.04},
    ],
    "Отдел кадров": [
        {"Таб. номер": "0001", "Фамилия": "Иванов И.И.", "Оклад": 6000.00, "Надбавки": 4000.00},
        {"Таб. номер": "0003", "Фамилия": "Сидоров С.С.", "Оклад": 5000.00, "Надбавки": 4500.00},
        {"Таб. номер": "0006", "Фамилия": "Львов Л.Л.", "Оклад": 4074.07, "Надбавки": 2444.44},
        {"Таб. номер": "0007", "Фамилия": "Волков В.В.", "Оклад": 1434.78, "Надбавки": 1434.78},
    ],
    "Столовая": [
        {"Таб. номер": "0004", "Фамилия": "Мишин М.М.", "Оклад": 5500.00, "Надбавки": 3500.00},
    ]
}

# Создаем Excel-файл
wb = Workbook()
ws = wb.active
ws.title = "Зарплаты"

# Заголовки таблицы
headers = [
    "Таб. номер", "Фамилия", "Отдел", "Сумма по окладу, руб.", "Сумма по надбавкам, руб.",
    "Сумма зарплаты, руб.", "НДФЛ, %", "Сумма НДФЛ, руб.", "Сумма к выдаче, руб."
]
ws.append(headers)

# Заполняем данные
ndfl_rate = 0.13  # 13%
row = 2
for dept, employees in data.items():
    dept_salary_total = 0
    dept_allowance_total = 0
    dept_gross_total = 0
    dept_ndfl_total = 0
    dept_net_total = 0

    for emp in employees:
        salary = emp["Оклад"] + emp["Надбавки"]
        ndfl = round(salary * ndfl_rate, 2)
        net_salary = round(salary - ndfl, 2)

        ws.append([
            emp["Таб. номер"], emp["Фамилия"], dept,
            round(emp["Оклад"], 2), round(emp["Надбавки"], 2),
            round(salary, 2), "13%", ndfl, net_salary
        ])

        # Суммы по отделу
        dept_salary_total += emp["Оклад"]
        dept_allowance_total += emp["Надбавки"]
        dept_gross_total += salary
        dept_ndfl_total += ndfl
        dept_net_total += net_salary
        row += 1

    # Итог по отделу
    ws.append([
        "", "", f"{dept} Итого",
        round(dept_salary_total, 2), round(dept_allowance_total, 2),
        round(dept_gross_total, 2), "", round(dept_ndfl_total, 2), round(dept_net_total, 2)
    ])
    row += 1

# Общий итог
ws.append([
    "", "", "Общий итог",
    sum(emp["Оклад"] for dept in data.values() for emp in dept),
    sum(emp["Надбавки"] for dept in data.values() for emp in dept),
    sum(emp["Оклад"] + emp["Надбавки"] for dept in data.values() for emp in dept),
    "", sum(round((emp["Оклад"] + emp["Надбавки"]) * ndfl_rate, 2) for dept in data.values() for emp in dept),
    sum(round((emp["Оклад"] + emp["Надбавки"]) - (emp["Оклад"] + emp["Надбавки"]) * ndfl_rate, 2) for dept in
        data.values() for emp in dept),
])

# Сохраняем файл
wb.save("Зарплаты.xlsx")
