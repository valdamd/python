def triangle_type(a, b, c):
    # Проверка неравенства треугольника
    if a + b > c and a + c > b and b + c > a:
        # Проверка на прямоугольный треугольник
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Прямоугольный треугольник"
        # Проверка на остроугольный треугольник
        elif a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
            return "Остроугольный треугольник"
        # Если не прямоугольный и не остроугольный, то тупоугольный
        else:
            return "Тупоугольный треугольник"
    else:
        return "Треугольник не существует"

# Пример использования
a, b, c = map(int, input("Введите стороны  пробел: ").split())
print(triangle_type(a, b, c))