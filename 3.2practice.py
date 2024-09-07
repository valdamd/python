import math
'''2.Напишите собственную функцию для поиска наибольшего
общего делителя двух натуральных чисел (НОД). Проверьте
работоспособность вашей функции по средствам сравнения
результата работы вашего алгоритма с результатом работы
аналогичной функции из пакета math.'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def validate_input(n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("Некорректный ввод. Введите натуральное число.")
        return n
    except ValueError as e:
        print(e)
        return None

def main():
    num1 = validate_input(input("Введите первое число: "))
    num2 = validate_input(input("Введите второе число: "))

    if num1 is not None and num2 is not None:
        result = gcd(num1, num2)
        print(f"НОД({num1}, {num2}) = {result}")


        assert result == math.gcd(num1, num2), "Результаты не совпадают"

if __name__ == "__main__":
    main()