# Задача №1

print("=" * 10 + " " + "Задача №1" + " " + "=" * 10, "\n")
num = num1 = int(input("Введите пятизначное число: "))
fifth = num % 10
num //= 10
fourth = num % 10
num //= 10
third = num % 10
num //= 10
second = num % 10
first = num // 10
pro = first * second * third * fourth * fifth
arif = (first + second + third + fourth + fifth) / 5
print("Произведение цифр числа " + str(num1) + ": " + str(pro))
print("Среднее арифметическое: " + str(arif))
print("=" * 7 + " " + "конец Задачи №1" + " " + "=" * 7, "\n")

# Задача №2

print("=" * 10 + " " + "Задача №2" + " " + "=" * 10, "\n")
num = int(input("Введите целое число: "))
if num % 2 == 0:
    print("Число " + str(num) + " - чётное")
else:
    print("Число " + str(num) + " - нечётное")
print("=" * 7 + " " + "конец Задачи №2" + " " + "=" * 7, "\n")

# Задача №3

print("=" * 10 + " " + "Задача №3" + " " + "=" * 10, "\n")
print('Выберите операцию:\n'
'1 - "r" - применяет унарный минуск операнду\n'
'2 - "+" - сложение\n'
'3 - "-" - вычитание\n'
'4 - "/" - деление\n'
'5 - "*" - умножение\n'
'6 - "%" - остаток от деления\n'
'7 - "<" - минимальное из двух чисел\n'
'8 - ">" - максимальное из двух чисел')
res = "Ответ:"
num = int(input("Введите номер операции: "))
if num == 1:
    unar = int(input("Введите число: "))
    unar = -unar
    print(res, unar)
if num == 2:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    print(res, first + second)
elif num == 3:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    print(res, first - second)
elif num == 4:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    if second == 0:
        print(res + "На 0 делить нельзя!")
    else:
        print(res, first / second)
elif num == 5:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    print(res, first * second)
elif num == 6:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    print(res, first % second)
elif num == 7:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    if first < second:
        print(res, str(first) + " меньше " + str(second))
    else:
        print(res, str(second) + " меньше " + str(first))
elif num == 8:
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    if first > second:
        print(res, str(first) + " больше " + str(second))
    else:
        print(res, str(second) + " больше " + str(first))
print("=" * 7 + " " + "конец Задачи №3" + " " + "=" * 7, "\n")

# Задача №4

print("=" * 10 + " " + "Задача №4" + " " + "=" * 10, "\n")
num = int(input("Введите число от 1 до 99: "))
if num % 10 == 1 and num // 10 % 10 != 1:
    print(num, "копейка")
elif num // 10 % 10 != 1 and (num % 10 == 2 or num % 10 == 3 or num % 10 == 4):
    print(num, "копейки")
else:
    print(num, "копеек")
print("=" * 7 + " " + "конец Задачи №4" + " " + "=" * 7, "\n")
