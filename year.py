god=int(input("Введите год: "))

if (god % 4 == 0) and (god % 100 != 0):
    print("Высокосный")
else:
    print("Нет")