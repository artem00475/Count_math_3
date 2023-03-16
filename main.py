from console_utils import *


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
    print("Метод левых прямоугольников")
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
    result = h*sum(y_table)
    flag = True
    while flag:
        n *= 2
        h = (b-a)/n
        x_table = [a]
        previous = a
        for i in range(n):
            previous += h
            x_table.append(previous)
        y_table = []
        for x in x_table:
            y_table.append(func(eq, x))
        r = h*sum(y_table)
        if abs(r - result) < accuracy:
            flag = False
        result = r
    print("Значение интеграла:", result)
    print("Число разбиения интервала", n)


def right_rectangles_method(eq, accuracy, a, b):
    print("Метод правых прямоугольников")
    n = 4
    h = (b - a) / n
    x_table = [a+h]
    previous = a+h
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
        x_table = [a+h]
        previous = a+h
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
    print("Значение интеграла:", result)
    print("Число разбиения интервала", n)


def middle_rectangles_method(eq, accuracy, a, b):
    print("Метод средних прямоугольников")
    n = 4
    h = (b - a) / n
    x_table = [a+h/2]
    previous = a+h/2
    for i in range(n-1):
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
        x_table = [a+h/2]
        previous = a+h/2
        for i in range(n-1):
            previous += h
            x_table.append(previous)
        y_table = []
        for x in x_table:
            y_table.append(func(eq, x))
        r = h * sum(y_table)
        if abs(r - result)/3 < accuracy:
            flag = False
        result = r
    print("Значение интеграла:", result)
    print("Число разбиения интервала", n)


def trapeze_method(eq, accuracy, a, b):
    print("Метод трапеций")
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
    result = h/2 * (y_table[0]+y_table[-1]+2*sum(y_table[1:-1]))
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
        r = h/2 * (y_table[0]+y_table[-1]+2*sum(y_table[1:-1]))
        if abs(r - result) / 3 < accuracy:
            flag = False
        result = r
    print("Значение интеграла:", result)
    print("Число разбиения интервала", n)


def simpson_method(eq, accuracy, a, b):
    print("Метод трапеций")
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
    result = h / 3 * (y_table[0] + y_table[-1] + 2 * sum(y_table[1:-1:2])+4*sum(y_table[2:-1:2]))
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
        r = h / 3 * (y_table[0] + y_table[-1] + 4 * sum(y_table[1:-1:2])+2*sum(y_table[2:-1:2]))
        if abs(r - result) / 15 < accuracy:
            flag = False
        result = r
    print("Значение интеграла:", result)
    print("Число разбиения интервала", n)


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
            print("ВЫберите метод:")
            print("1. Метод левых прямоугольников")
            print("2. Метод правых прямоугольников")
            print("3. Метод средних прямоугольников")
            print("4. Метод трапеций")
            print("5. Метод Симпсона")
            method = enter_value(1, 5)
            ac, begin, end = get_data(equation)
            if method == 1:
                left_rectangles_method(equation, ac, begin, end)
            elif method == 2:
                right_rectangles_method(equation, ac, begin, end)
            elif method == 3:
                middle_rectangles_method(equation, ac, begin, end)
            elif method == 4:
                trapeze_method(equation, ac, begin, end)
            else:
                simpson_method(equation, ac, begin, end)
        except ValueError:
            print("Ошибка в введенном уравнении")
    else:
        print()
        # f = open("equations1.txt")
        # count = int(f.readline())
        # print("Выбирите подинтегральную функцию:")
        # equations = []
        # try:
        #     for x in range(1, count + 1):
        #         e = f.readline().replace('\n', '')
        #         s = str(x) + '. ' + e
        #         equations.append(to_pol_format(e))
        #         print(s)
        #     number = enter_value(1, count)
        #     equation = equations[number - 1]
        #     print("Выберите метод:")
        #     print("1. Метод левых прямоугольников")
        #     print("2. Метод правых прямоугольников")
        #     print("3. Метод средних прямоугольников")
        #     print("4. Метод трапеций")
        #     print("5. Метод Симпсона")
        #     method = enter_value(1, 5)
        #     if method == 1:
        #         left_rectangles_method(equation, number)
        #     elif method == 2:
        #         right_rectangles_method(equation, number)
        #     elif method == 3:
        #         middle_rectangles_method(equation, number)
        #     elif method == 4:
        #         trapeze_method(equation, number)
        #     else:
        #         simpson_method(equation, number)
        # except ValueError:
        #     print("Ошибка в введенном уравнении")
    while True:
        ans = input("Решить еще одно уравнение? (y/n)\n")
        if ans == 'n':
            work = False
            break
        elif ans == 'y':
            break
