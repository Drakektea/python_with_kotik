from math import tan, atan, sqrt, pi


'''
Запишите арифметическое выражение на языке Python в виде строки,
а затем выведите полученный результат на экран:
3tg|√(x + y^2) - π| - arctg^3(√x + y^2).
'''
y = 1
x = 2

answer = 3 * tan(abs(sqrt(x + y ** 2) - pi)) - atan(sqrt(x) + y ** 2) ** 3
print(answer)


