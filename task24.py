from random import randint
list = list(randint(1, 9) for i in range(int(input("Введите кол-во кустов: "))))
print(list)
a = int(input("Введите номер куста: "))
res = 0
if a == 1:
    res = list[0] + list[1] + list[-1]
elif a == len(list):
    res = list[-2] + list[-1] + list[0]
else:
    res = list[a-1] + list[a-2] + list[a]
print(res, "ягод черники собрано")