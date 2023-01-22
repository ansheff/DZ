print("Введите элементы списка:")
element = [int(input("-> ")) for _ in range(int(input("n = ")))]
for i in range(1, len(element)):
    if element[i] > element[i - 1]:
        print(element[i], end=" ")
