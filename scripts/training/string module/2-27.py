'''
Подсчитайте количество русских букв в строке 'Camel - это же
верблюд, а не ёж!' и выведите результат на экран. В таблице
символов Юникода строчные буквы русского алфавита занимают
диапазон номеров с 1040 по 1103, а также 1025 и 1105 для букв
Ё и ё.
'''

txt = 'Camel - это же верблюд, а не ёж!'
russian_alphabetic = {chr(i) for i in range(1040, 1104)} | {chr(1025), chr(1105)}
russian_chars = [char for char in txt if char in russian_alphabetic]
print(len(russian_chars))
