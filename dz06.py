# Задача №1
element = [int(input("Введите элемент списка: ")) for _ in range(int(input("Введите длину списка: ")))]
lst = lst1 = []
for i in range(len(element)):
    lst = list(element)
print("Список:", lst)
for i in lst:
    if i > 0:
        lst1.append(i)
print("Новый список, состоящий из положительных элементов:", lst1)
largest = lst1[0]
for i in range(1, len(lst1)):
    if lst1[i] > largest:
        largest = lst1[i]
print("Наибольший элемент списка:", largest)

# Задача №2
print("Введите элементы списка:")
element = [int(input("-> ")) for _ in range(int(input("n = ")))]
lst = []
for i in range(len(element)):
    lst = list(element)
k = int(input('Введите индекс: '))
print("k =", k)
c = int(input("Введите значение: "))
print("c =", c)
lst.insert(k, c)
print(lst)

# Задача №3
print("Введите элементы списка:")
element = [int(input("-> ")) for _ in range(int(input("n = ")))]
lst = []
for i in range(len(element)):
    lst = list(element)
ch = int(input("Введите число: "))
print("ch =", ch)
if ch in lst:
    print("Число присутствует в элементах списка")
else:
    print("Число отсутствует в элементах списка")
