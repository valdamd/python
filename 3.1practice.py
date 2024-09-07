import math
"""1.Считайте с консоли величину угла на плоскости в градусах.
Используя методы или функции библиотеки math, определите
и выведите на консоль синус, косинус и тангенс этого угла. Не
забудьте учесть, в каких единицах должны быть переданы
аргументы соответствующих методов: в градусах или радианах."""
def get_angle_from_user():
    while True:
        try:
            angle = float(input("Введите угол в градусах: "))
            if angle < 0 or angle > 360:
                raise ValueError("Угол должен быть в диапазоне от 0 до 360.")
            return angle
        except ValueError as e:
            print(e)

def calculate_trigonometric_functions(angle):
    radian_angle = math.radians(angle)
    sine = math.sin(radian_angle)
    cosine = math.cos(radian_angle)
    tangent = math.tan(radian_angle)
    return sine, cosine, tangent

def main():
    angle = get_angle_from_user()
    sine, cosine, tangent = calculate_trigonometric_functions(angle)
    print(f"Синус угла: {sine}")
    print(f"Косинус угла: {cosine}")
    print(f"Тангенс угла: {tangent}")

if __name__ == "__main__":
    main()