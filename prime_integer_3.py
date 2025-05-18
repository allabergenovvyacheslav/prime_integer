"""
Задача с кодом. Наибольшее простое число в диапазоне

Напишите функцию, которая будет принимать начальное и конечное значения диапазона чисел и возвращать наибольшее
простое число в этом диапазоне.

Примечания:

- В функцию будут передаваться только положительные целые числа.
- Простое число — такое целое положительное число, которое делится только на себя и на единицу.
"""


def fat_prime(a, b):
    prime_num = []
    if a < b:
        norms_num = [i for i in range(a, b + 1)]
        for number in norms_num:
            prime = True
            if number <= 1:
                prime = False
            else:
                for i in range(2, int(number ** 0.5 + 1)):
                    if number % i == 0:
                        prime = False
                        break
            if prime is True:
                prime_num.append(number)
        print(max(prime_num))
    else:
        a, b = b, a
        revers_num = [i for i in reversed(range(a, b + 1))]
        for number in revers_num:
            prime = True
            if number <= 1:
                prime = False
            else:
                for i in range(2, int(number ** 0.5 + 1)):
                    if number % i == 0:
                        prime = False
                        break
            if prime is True:
                prime_num.append(number)
        print(max(prime_num))




fat_prime(125, 44)


