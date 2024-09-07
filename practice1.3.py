sum_digits = int(input("Введите сумму цифр: "))

# Проверяем все трехзначные числа
for num in range(100, 1000):
    # Преобразуем число в строку и считаем сумму его цифр
    digit_sum = sum(map(int, str(num)))

    # Если сумма цифр равна заданной, печатаем число
    if digit_sum == sum_digits:
        print(num)