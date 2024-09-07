
def is_lucky_ticket(ticket):
    # Преобразуем билет в строку и разделяем на первые три цифры и последние три
    first_three_digits = int(ticket[:3])
    last_three_digits = int(ticket[3:])
    3:
    # Проверяем, равны ли суммы цифр
    return sum(map(int, str(first_three_digits))) == sum(map(int, str(last_three_digits)))

# Вводим границы диапазона
N = int(input("Введите меньший номер билета: "))
M = int(input("Введите больший номер билета: "))

# Считаем количество счастливых билетов
count = sum(is_lucky_ticket(str(i)) for i in range(N, M + 1))

# Выводим результат
print("Количество счастливых билетов:", count)