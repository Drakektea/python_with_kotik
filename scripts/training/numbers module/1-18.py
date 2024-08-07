from math import cos, sin


'''
Запишите арифметическое выражение на языке Python в виде строки,
а затем выведите полученный результат на экран: cos^2(3a - 1) -
sin(5a - b)^3.
'''

a = 2
b = 1
answer = cos(3 * a - 1) ** 2 - sin((5 * a - b) ** 3)
print(answer)


