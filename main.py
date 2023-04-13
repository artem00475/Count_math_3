import sympy

from console_utils import *
from sympy import *


def get_data(eq):
    accuracy = get_accuracy()
    a, b = get_interval(eq, accuracy)
    return accuracy, a, b


# Преобразование уравнения в обратную польскую запись
def to_pol_format(st):
    a = st.split()
    res = []
    op = []
    symb = {'-': 0, '+': 0, '*': 1, '^': 2, 'cos': 3, 'sin': 3}
    for s in a:
        if s not in symb:
            if s != "x" and s != "x_1" and s != "x_2":
                res.append(float(s))
            else:
                res.append(s)
        else:
            if len(op) == 0:
                op.append(s)
            else:
                sm = op.pop()
                if symb[s] <= symb[sm]:
                    res.append(sm)
                    while len(op) > 0 and symb[s] <= symb[op[-1]]:
                        sm = op.pop()
                        res.append(sm)
                else:
                    op.append(sm)
                op.append(s)
    while len(op) > 0:
        res.append(op.pop())
    return res


def left_rectangles_method(eq, accuracy, a, b):
    n = 4
    h = (b - a) / n
    x_table = [a]
    previous = a
    for i in range(n):
        previous += h
        x_table.append(previous)
    y_table = []
    for x in x_table:
        y_table.append(func(eq, x))
    result = h * sum(y_table)
    flag = True
    while flag:
        n *= 2
        h = (b - a) / n
        x_table = [a]
        previous = a
        for i in range(n):
            previous += h
            x_table.append(previous)
        y_table = []
        for x in x_table:
            y_table.append(func(eq, x))
        r = h * sum(y_table)
        if abs(r - result) < accuracy:
            flag = False
        result = r
    return result, n


def right_rectangles_method(eq, accuracy, a, b):
    n = 4
    h = (b - a) / n
    x_table = [a + h]
    previous = a + h
    for i in range(n):
        previous += h
        x_table.append(previous)
    y_table = []
    for x in x_table:
        y_table.append(func(eq, x))
    result = h * sum(y_table)
    flag = True
    while flag:
        n *= 2
        h = (b - a) / n
        x_table = [a + h]
        previous = a + h
        for i in range(n):
            previous += h
            x_table.append(previous)
        y_table = []
        for x in x_table:
            y_table.append(func(eq, x))
        r = h * sum(y_table)
        if abs(r - result) < accuracy:
            flag = False
        result = r
    return result, n


def middle_rectangles_method(eq, accuracy, a, b):
    n = 4
    h = (b - a) / n
    x_table = [a + h / 2]
    previous = a + h / 2
    for i in range(n - 1):
        previous += h
        x_table.append(previous)
    y_table = []
    for x in x_table:
        y_table.append(func(eq, x))
    result = h * sum(y_table)
    flag = True
    while flag:
        n *= 2
        h = (b - a) / n
        x_table = [a + h / 2]
        previous = a + h / 2
        for i in range(n - 1):
            previous += h
            x_table.append(previous)
        y_table = []
        for x in x_table:
            y_table.append(func(eq, x))
        r = h * sum(y_table)
        if abs(r - result) / 3 < accuracy:
            flag = False
        result = r
    return result, n


def trapeze_method(eq, accuracy, a, b):
    n = 4
    h = (b - a) / n
    x_table = [a]
    previous = a
    for i in range(n):
        previous += h
        x_table.append(previous)
    y_table = []
    for x in x_table:
        y_table.append(func(eq, x))
    result = h / 2 * (y_table[0] + y_table[-1] + 2 * sum(y_table[1:-1]))
    flag = True
    while flag:
        n *= 2
        h = (b - a) / n
        x_table = [a]
        previous = a
        for i in range(n):
            previous += h
            x_table.append(previous)
        y_table = []
        for x in x_table:
            y_table.append(func(eq, x))
        r = h / 2 * (y_table[0] + y_table[-1] + 2 * sum(y_table[1:-1]))
        if abs(r - result) / 3 < accuracy:
            flag = False
        result = r
    return result, n


def simpson_method(eq, accuracy, a, b):
    n = 4
    h = (b - a) / n
    x_table = [a]
    previous = a
    for i in range(n):
        previous += h
        x_table.append(previous)
    y_table = []
    for x in x_table:
        y_table.append(func(eq, x))
    result = h / 3 * (y_table[0] + y_table[-1] + 2 * sum(y_table[1:-1:2]) + 4 * sum(y_table[2:-1:2]))
    flag = True
    while flag:
        n *= 2
        h = (b - a) / n
        x_table = [a]
        previous = a
        for i in range(n):
            previous += h
            x_table.append(previous)
        y_table = []
        for x in x_table:
            y_table.append(func(eq, x))
        r = h / 3 * (y_table[0] + y_table[-1] + 4 * sum(y_table[1:-1:2]) + 2 * sum(y_table[2:-1:2]))
        if abs(r - result) / 15 < accuracy:
            flag = False
        result = r
    return result, n


work = True
while work:
    print("Выберите, что хотите решить:")
    print("1. Определенный интеграл")
    print("2. Несобственный интеграл")
    if enter_value(1, 2) == 1:
        f = open("equations.txt")
        count = int(f.readline())
        print("Выбирите подинтегральную функцию:")
        equations = []
        try:
            for x in range(1, count + 1):
                e = f.readline().replace('\n', '')
                s = str(x) + '. ' + e
                equations.append(to_pol_format(e))
                print(s)
            number = enter_value(1, count)
            equation = equations[number - 1]
            # print(equation)
            # print(antiderivative(equation))
            antif = antiderivative(equation)
            print("ВЫберите метод:")
            print("1. Метод левых прямоугольников")
            print("2. Метод правых прямоугольников")
            print("3. Метод средних прямоугольников")
            print("4. Метод трапеций")
            print("5. Метод Симпсона")
            method = enter_value(1, 5)
            ac, begin, end = get_data(equation)
            if method == 1:
                print("Метод левых прямоугольников")
                r, c = left_rectangles_method(equation, ac, begin, end)
            elif method == 2:
                print("Метод правых прямоугольников")
                r, c = right_rectangles_method(equation, ac, begin, end)
            elif method == 3:
                print("Метод средних прямоугольников")
                r, c = middle_rectangles_method(equation, ac, begin, end)
            elif method == 4:
                print("Метод трапеций")
                r, c = trapeze_method(equation, ac, begin, end)
            else:
                print("Метод Симпсона")
                r, c = simpson_method(equation, ac, begin, end)
            print("Значение интеграла:", r)
            print("Число разбиения интервала", c)
            left_val = func(antif, begin)
            right_val = func(antif, end)
            print("Точное значение:", right_val - left_val)
            print("Абсолютное отклонение:", abs(right_val - left_val - r))
        except ValueError:
            print("Ошибка в введенном уравнении")
    else:
        print()
        f = open("equations1.txt")
        count = int(f.readline())
        print("Выбирите подинтегральную функцию:")
        equations = []
        try:
            for x in range(1, count + 1):
                e = f.readline().replace('\n', '')
                s = str(x) + '. ' + e
                equations.append(to_pol_format(e))
                print(s)
            number = enter_value(1, count)
            equation = equations[number - 1]
            print("Выберите метод:")
            print("1. Метод левых прямоугольников")
            print("2. Метод правых прямоугольников")
            print("3. Метод средних прямоугольников")
            print("4. Метод трапеций")
            print("5. Метод Симпсона")
            method = enter_value(1, 5)
            ac, begin, end = get_data(equation)
            # print(equation)
            # print(antiderivative(equation))
            antif = antiderivative(equation)
            try:
                # if number == 1 and begin <= 0 <= end:
                #     raise ArithmeticError
                interval, symbols = check_interval(equation, begin, end, ac)
                r, c = 0, 0
                r1, c1 = 0, 0
                left_val, right_val = 0, 0
                left_val1, right_val1 = 0, 0
                #print(interval)
                if len(interval) == 2:
                    left_val = func(antif, begin)
                    right_val = func(antif, end)
                    begin, end = interval[0], interval[1]
                    if method == 1:
                        r, c = left_rectangles_method(equation, ac, begin, end)
                    elif method == 2:
                        r, c = right_rectangles_method(equation, ac, begin, end)
                    elif method == 3:
                        r, c = middle_rectangles_method(equation, ac, begin, end)
                    elif method == 4:
                        r, c = trapeze_method(equation, ac, begin, end)
                    else:
                        r, c = simpson_method(equation, ac, begin, end)
                else:
                    begin, middle, end = interval[0], interval[1], interval[2]
                    func(antif, middle)
                    left_val = func(antif, begin)
                    right_val = func(antif, middle)
                    left_val1 = func(antif, middle)
                    right_val1 = func(antif, end)
                    if method == 1:
                        r, c = left_rectangles_method(equation, ac, begin, middle-ac)
                        r1, c1 = left_rectangles_method(equation, ac, middle+ac, end)
                    elif method == 2:
                        r, c = right_rectangles_method(equation, ac, begin, middle-ac)
                        r1, c1 = right_rectangles_method(equation, ac, middle+ac, end)
                    elif method == 3:
                        r, c = middle_rectangles_method(equation, ac, begin, middle-ac)
                        r1, c1 = middle_rectangles_method(equation, ac, middle+ac, end)
                    elif method == 4:
                        r, c = trapeze_method(equation, ac, begin, middle-ac)
                        r1, c1 = trapeze_method(equation, ac, middle+ac, end)
                    else:
                        r, c = simpson_method(equation, ac, begin, middle-ac)
                        r1, c1 = simpson_method(equation, ac, middle+ac, end)
                print("Значение интеграла:", r+r1)
                print("Число разбиения интервала", c+c1)
                print("Точное значение:", right_val + right_val1 - left_val - left_val1)
                print("Абсолютное отклонение:", abs(right_val + right_val1 - left_val - left_val1 - r - r1))
            except ZeroDivisionError:
                print("Интеграл не существует")
        except ValueError:
            print("Ошибка в введенном уравнении")
    while True:
        ans = input("Решить еще одно уравнение? (y/n)\n")
        if ans == 'n':
            work = False
            break
        elif ans == 'y':
            break
