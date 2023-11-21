#!/usr/bin/env python3
import math


def cylinder():

    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    def circle():
        return math.pi * radius ** 2

    lateral_area = 2 * math.pi * radius * height
    total_area = lateral_area + 2 * circle()

    choice = input("Хотите получить только площадь боковой поверхности (введите 'да' или 'нет')? ").lower()

    if choice == 'да':
        print(f"Площадь боковой поверхности цилиндра: {lateral_area:.2f}")
    elif choice == 'нет':
        print(f"Полная площадь цилиндра: {total_area:.2f}")
    else:
        print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")


if __name__ == "__main__":
    cylinder()
