# coding=windows-1251
from random import randint
from pyDatalog import pyDatalog
number = 10

pyDatalog.create_terms('A, B, Res, Sum, Avg, Range, RandSum, Median, Rand')

(Sum[Range] == sum_(A, for_each = A)) <= A.in_(range_(Range + 1))
print(f"Сумма чисел от 0 до {number}:\n")
print(f"{Sum == Sum[number]}\n")

(Avg[Range] == Res) <= (Range / 2 == Res)
print(f"Среднее значение:\n")
print(f"{Avg == Avg[number]}\n")

randlist = [randint(0, 99) for _ in range(0, 100)]
randlist.sort()

(Sum[Rand] == sum_(A, for_each = A)) <= A.in_(Rand)
print(f"Сумма 100 случайных чисел:\n")
print(f"{Sum[randlist] == RandSum}\n")

print(f"медиана:\n")
(Median[Rand] == Res) <= ((Rand[49] + Rand[50]) / 2 == Res)
print(Median[randlist] == Median)
