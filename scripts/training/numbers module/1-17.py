from math import sqrt, log, log10, log2, e


'''
Вычислите значение арифметического выражения при заданных
значениях переменных и выведите полученный результат на экран:
√(log2(mn+2 - 3e)):(ln(2m) + lg(4n)) при m=5, n=2.
'''

m = 5
n = 2

answer = sqrt(log2(m * n + 2 - 3 * e)) / (log(2 * m) + log10(4 * n))
print(answer)
