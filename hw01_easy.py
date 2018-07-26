import random

__author__ = 'Воскобоев Глеб Александрович'


# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

# код пишем тут...
def first():
    def rnum():  # получаем рандомное число
        num = random.randint(0, 1000001)
        print('Рандомно сгенерированое число: %s' % num)
        return num

    def while_(num):
        while num != 0:
            dig = num % 10
            print(dig)
            num = num // 10

    def for_(num):
        for dig in str(abs(num)):
            print(dig)

    while_(rnum())
    print()
    for_(rnum())


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
def second():
    a = input('Первая переменная: ')
    b = input('Вторая переменная: ')
    a, b = b, a
    print('Первая переменная теперь равна: %s,' % a)
    print('а вторая: %s' % b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
def third():
    def input_():
        while True:
            try:
                a = int(input('Введите свой возраст: '))
                break
            except ValueError:
                print('Введите число.')
        return a


    a = input_()

    if a >= 18:
        print('Доступ разрешён')
    else:
        print('Извините, пользование данным ресурсом только с 18 лет')


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
    print()


console_out()