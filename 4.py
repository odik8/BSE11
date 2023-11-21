#!/usr/bin/env python3

def get_input():
    return str(input("Введите строку: "))


def test_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(value):
    try:
        result = int(value)
        return result
    except ValueError:
        return None


def print_int(value):
    print(value)


if __name__ == "__main__":
    input_value = get_input()

    if test_input(input_value):
        converted_value = str_to_int(input_value)

        if converted_value is not None:
            print_int(converted_value)
        else:
            print("Не удалось выполнить преобразование.")
    else:
        print("Введенное значение не может быть преобразовано в целое число.")
