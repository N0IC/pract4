def geometric_progression_nth_term(a, b, c):
    if n == 1:
        return a
    else:
        return b * geometric_progression_nth_term(a, b, c - 1)


def geometric_progression_sum(a, b, c):
    if c == 1:
        return a
    else:
        return geometric_progression_nth_term(a, b, c) + geometric_progression_sum(a, b, c - 1)


def arithmetic_progression_nth_term(a, b, c):
    if c == 1:
        return a
    else:
        return arithmetic_progression_nth_term(a, b, c - 1) + b


def decimal_to_binary(a):
    if a == 0:
        return ''
    else:
        return decimal_to_binary(a // 2) + str(a % 2)


n = int(input(f'1)n-й член геом. прогрессии: \n'
              f'2) сумму n членов геометрической прогрессии: \n'
              f'3) n-й член арифметической прогрессии: \n'
              f'4) двоичное представление десятичного числа: \n'))
if n == 1:
    a = int(input('Введите число а: '))
    b = int(input('Введите число b: '))
    c = int(input('Введите число c: '))
    print(geometric_progression_nth_term(a, b, c))
elif n == 2:
    a = int(input('Введите число а: '))
    b = int(input('Введите число b: '))
    c = int(input('Введите число c: '))
    print(geometric_progression_sum(a, b, c))
elif n == 3:
    a = int(input('Введите число а: '))
    b = int(input('Введите число b: '))
    c = int(input('Введите число c: '))
    print(arithmetic_progression_nth_term(a, b, c))
else:
    print('Функция не найдена')
