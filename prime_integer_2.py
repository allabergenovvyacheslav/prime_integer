'''
Вспомним, что простые числа — те натуральные числа, у которых два делителя: оно само и 1.
Напишите программу для определения количества простых чисел среди введённых.

Формат ввода
В первой строке записано число N Во всех последующих N строках — по одному числу.

Формат вывода
Требуется вывести общее количество простых чисел среди введённых (кроме N).
'''

iterations = int(input())
result = 0
prime_num = []
for _ in range(iterations):
    prime = True
    number = int(input())
    if number <= 1:
        prime = False
    else:
        for i in range(2, int(number ** 0.5 + 1)):
            if number % i == 0:
                prime = False
                break
    if prime is True:
        prime_num.append(str(number))
        result += 1
print(f'Здесь {result} простых числа {prime_num}')

