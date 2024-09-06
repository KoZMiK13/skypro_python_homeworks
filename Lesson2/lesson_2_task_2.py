def is_year_leap():
    return "Да" if year % 4 == 0 else "Нет"


year = int(input("Введите год: "))
result = is_year_leap()
print(f"Является ли год {year} високосным? - {result}")
