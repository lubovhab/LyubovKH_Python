def is_year_leap(num):
    return True if num % 4 == 0 else False


number = int(input("Введите год: "))
result = is_year_leap(number)

print(f"год {number}: {result}")
