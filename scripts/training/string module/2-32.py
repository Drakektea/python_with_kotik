'''
Измените строку 'Чья это корова там замычала?' таким образом,
чтобы символы в словах были записаны в обратном порядке.
Разделителем слов считайте пробел. Выведите результат на экран.
'''

txt = 'Чья это корова там замычала?'
txt = txt.split()
print(txt)
txt = [word[::-1] for word in txt]
print(' '.join(txt))

