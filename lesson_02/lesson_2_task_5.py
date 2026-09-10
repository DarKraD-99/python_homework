def month_to_season(nums):
    if nums in [12, 1, 2]:
        return "Зима"
    elif nums in [3, 4, 5]:
        return "Весна"
    elif nums in [6, 7, 8]:
        return "Лето"
    elif nums in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный месяц"


nums = int(input("Введите месяц от 1-12 "))
print(month_to_season(nums))
