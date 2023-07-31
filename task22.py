from random import randint
n_list = list(randint(1, 20) for i in range(int(input("Введите кол-во элементов первого множества: "))))
print(n_list)
m_list = list(randint(1, 20) for i in range(int(input("Введите кол-во элементов второго множества: "))))
print(m_list)
print("Элементы множеств n и m:", sorted(set(n_list)|set((m_list))))