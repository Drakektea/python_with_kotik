'''
Определите совпадает ли количество круглых открывающихся и
круглых закрывающихся скобок в строке 'abs(math.sin(pow((5*a -
b), 3)))'. Выведите результат проверки на экран в виде сообщения.
'''

txt = 'abs((math.sin(pow((5*a -b), 3)))'
print(txt.count('(') == txt.count(')'))


