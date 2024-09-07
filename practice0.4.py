import math

def vector_length(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

# Пример использования
x, y, z = map(float, input("Введите координаты вектора через пробел: ").split())
length = vector_length(x, y, z)
print(f"Длина вектора: {length}")