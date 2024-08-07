'''
Найдите наименьшую обыкновенную дробь,
равную вещественному числу 14.375, и выведите ее на экран в формате '14.375 = числитель/знаменатель'.
'''

num = 0.75
numerator, denominator = num.as_integer_ratio()
print(num, "=", numerator, "/", denominator)
