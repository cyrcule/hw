import math
import random

__author__ = 'Воскобоев Глеб Александрович'


# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
def first():
    def rnum():  # получаем рандомное число
        num = random.randint(0, 1000001)
        print('Рандомно сгенерированое число: %s' % num)
        return num

    num = rnum()

    print('Наибольшая цифра: %s' % max(list(str(num))))


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
def second():
    a = input('Первая переменная: ')
    b = input('Вторая переменная: ')
    a, b = b, a
    print('Первая переменная теперь равна: %s,' % a)
    print('а вторая: %s' % b)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4
def third():
    def input_():
        # функция для проверки вводимых данных на соответствие условиям задачи
        def input_check(str, var_name, zcheck = False):
            # функция для фильтрации и перезаписи переменной если она равна '0'
            def zero_check(str):
                while str == '0' or 0:
                    print('"%s" не может равняться 0, введите другое значение.' %var_name)
                    str = input('a = ')
                    str = is_digit(str) # защита от повторного введения 0 на следующем этапе
                return str
            # функция для проверки является ли введёное пользователем занчение числом,\
            # а также перезаписи если это не так
            def is_digit(string):
                while True:
                    if string.isdigit():
                        break
                    else:
                        try:
                            float(string)
                            break
                        except ValueError:
                            print('Введёное значение не являетсся числом.')
                            string = input('%s = ' %var_name)
                            continue
                return string

            if zcheck:
                str = zero_check(str)
            else:  # в случае если была проведена проверка на равность 0 проводить повторную проверку \
                #  на соответствия символа числу не имеет смысла
                str = is_digit(str)

            return str

        a = float(input_check(input('a = '), 'a', True))
        b = float(input_check(input('b = '), 'b'))
        c = float(input_check(input('c = '), 'c'))


        return a, b, c

    print('ax^2 + bx + c = 0:')
    a, b, c = input_()

    d = b ** 2 - 4 * a * c
    print("Дискриминант d = %.2f" % d)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif d == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")


def console_out():
    print('Автор: %s\n' % __author__)

    print('Задание #1')
    first()
    print()

    print('Задание #2')
    second()
    print()

    print('Задание #3')
    third()


console_out()
