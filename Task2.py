# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input('Введите число n: '))
my_list = []
sum = 0
for i in range(1, n+1):
    num = (1 + 1/i)**i
    my_list.append(num)

print(my_list)

for i in my_list:
    sum += i
print(round(sum, 2))
