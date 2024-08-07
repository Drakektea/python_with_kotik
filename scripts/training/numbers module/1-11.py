from math import sin, cos, pi, radians


'''
Выведите на экран результат вычисления sin(π/6) и cos(45°)
округлив результат до двух знаков после десятичной точки.
'''
num1 = round(sin(pi / 6), 2)
num2 = round(cos(radians(45)), 2)

print(num1, num2)

