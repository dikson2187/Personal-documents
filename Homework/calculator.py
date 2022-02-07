import math

print("Добро пожаловать в калькулятор!\n")


while True:

    number_1 = int(input("Введите первое число --->"))
    number_2 = int(input("Введите второе число --->"))
    print("Выберите операцию:\n+ [сложение];\n- [вычитаение];\n* [умножение];"
          "\n/ [деление];\nstop [выход из программы]\n")
    sing = input("Введите желаемую операцию --->")

    if sing == "+":
        print('{} + {} ='.format(number_1, number_2), (number_1 + number_2),"\n" "log = ", math.log2(number_1 + number_2))
    elif sing == "-":
        print('{} - {} = '.format(number_1, number_2), (number_1 - number_2))
    elif sing == "*":
        print('{} * {} = '.format(number_1, number_2), (number_1 * number_2))
    elif sing == "/":
        if number_2 == 0:
            print("Введите другое число отличное от 0")
            continue
        else:
            print('{} / {} = '.format(number_1, number_2), (number_1 / number_2))
    elif sing == "stop":
        print("Выход из программы")
        break
    else:
        print("Проверте данные")


