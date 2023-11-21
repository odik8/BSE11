#!/usr/bin/env python3

def multiply_until_zero():
    product = 1
    while True:
        try:
            num = float(input("Введите число (введите 0 для завершения): "))
            if num == 0:
                break
            product *= num
            print(f"Результат умножения: {product}")
        except ValueError:
            print("Пожалуйста, введите корректное число.")


if __name__ == "__main__":
    multiply_until_zero()
