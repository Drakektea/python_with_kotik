int_num = int() + 1  # целое число
float_num = float() + 1  # число с плавающей точкой
complex_num = complex() + 1  # комплексное число

print(f'{int_num = }\n{float_num = }\n\n{complex_num = }')

# при работе с комплексными числами
real_part = complex_num.real  # реальная часть комплексного значения
image_part = complex_num.imag  # мнимая часть комплексного значения

print(f'{real_part = }\n{image_part = }')
