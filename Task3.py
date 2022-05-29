# Реализуйте алгоритм перемешивания списка.

# Вариант №1 - использование метода shuffle:

import random

my_list = [1, 2, 3, 4, 5]
print(f'Первоначальный вариант списка: {my_list}')
random.shuffle(my_list)
print(f'Перемешанный список: {my_list}')

# Вариант №2 - использование цикла for:

my_list = [1, 2, 3, 4, 5]
print(f'Первоначальный вариант списка: {my_list}')
for i in range(0, len(my_list) -1):
    j = random.randint(0, i+1)
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(f'Перемешанный список: {my_list}')