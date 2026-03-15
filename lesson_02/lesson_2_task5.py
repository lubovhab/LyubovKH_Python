month = int(input("Ведите номер месяца от 1 до 12: "))


def month_to_season(month):
    if (3 <= month <= 5):
        return "Весна"
    elif (6 <= month <= 8):
        return "Лето"
    elif (9 <= month <= 11):
        return "Осень"
    elif ((1 <= month <= 2) or (month == 12)):
        return "Зима"
    else:
        return "No valid"


print(f"Время года: {month_to_season(month)}")
