from math import acos, asin, atan, sqrt, pi


'''
Запишите арифметическое выражение на языке Python в виде строки,
а затем выведите полученный результат на экран:
√(arccos3x - arcsin2y)/arctg|x2 - y2| + 5√π.
'''
x = 0.1
y = 0.2
answer = sqrt(acos(3 * x) - asin(2 * y)) / atan(abs(x ** 2 - y ** 2)) + pi ** (1 / 5)
print(answer)

