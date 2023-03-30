from func_utils import *


# Считывание числа с клавиатуры
def enter_value(b, c):
    a = 0
    while a < b or a > c:
        try:
            a = int(input())
            if a < b or a > c:
                raise ValueError
        except ValueError:
            print("Повторите ввод")
    return a


# Считывание точности с клавиатуры
def get_accuracy():
    print("Введите желаемую точность в виде десятичной дроби")
    accuracy = False
    while not accuracy:
        try:
            accuracy = float(input())
            if accuracy <= 0 or accuracy >= 1:
                accuracy = False
                raise ValueError
        except ValueError:
            print("Повторите ввод")
    return accuracy


# Считывание интервала для нахождения корня с клавиатуры
def get_interval(eq, accur):
    # while True:
    print("Введите левую границу интервала")
    flaga = False
    a = 0
    while not flaga:
        try:
            a = float(input())
            flaga = True
        except ValueError:
            print("Повторите ввод")
    print("Введите правую границу интервала")
    flagb = False
    b = 0
    while not flagb:
        try:
            b = float(input())
            flagb = True
        except ValueError:
            print("Повторите ввод")
    # exist, a, b = check_interval(eq, a, b, accur)
    # if exist:
    #     return a, b
    # print("На данном интервале нет корней. Повторите ввод")
    return a, b


def check_interval(eq, a, b, accuracy):
    inter = []
    symb = []
    try:
        func(eq, a)
        inter.append(a)
        symb.append("/")
    except ZeroDivisionError:
        inter.append(a+accuracy)
        symb.append("+")
    i = inter[0]+accuracy
    while i < b:
        try:
            func(eq, i)
        except ZeroDivisionError:
            inter.append(i)
            symb.append("/")
        i += accuracy
        i = round(i, 10)
    try:
        func(eq, b)
        inter.append(b)
        symb.append("/")
    except ZeroDivisionError:
        inter.append(b - accuracy)
        symb.append("-")
    return inter, symb

