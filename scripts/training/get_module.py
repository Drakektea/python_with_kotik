import os
import requests
from bs4 import BeautifulSoup
from re import match


def wrap_text(text, max_length=63):
    words = text.split()
    wrapped_lines = []
    current_line = ''

    for word in words:
        if len(current_line + word) + 1 > max_length + 1 and word.endswith('.'):
            current_line += ' ' + word
            wrapped_lines.append(current_line)
            current_line = ''
            continue
        if len(current_line + word) + 1 > max_length + 1:
            wrapped_lines.append(current_line)
            current_line = ' ' + word
            continue
        if len(current_line) == 0:
            current_line += word
        else:
            current_line += ' ' + word
    else:
        wrapped_lines.append(current_line)

    return '\n'.join(line.strip() for line in wrapped_lines)


def clear_nt(text: str) -> str:
    return ''.join(''.join(text.split('\t')).split('\n')).strip()


module_count = input("Введите номер модуля: ")
catalog_name = input("Введите имя каталога: ")
from_task_count = input("Введите номер задания(с какого): ") or '0'
to_task_count = input("Введите номер задания(по какой): ") or 'inf'

if not os.path.exists(catalog_name):
    os.makedirs(catalog_name)

url = r"https://okpython.net/python/python_zadachnik/python_zadachnik.html"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    all_module_tasks = []
    is_in_module = False
    for div in soup.find_all("div", class_="content_div"):
        span = div.find("span", class_="light_bold smaller_font")
        if not span:
            continue

        start = str(span).find('t">') + len('t">')
        end = str(span).find('.<')
        pattern = fr'^{module_count}\.\d+\.$'
        if match(pattern, str(span)[start:end + 1]):
            all_module_tasks.append(div)

    for div in all_module_tasks:
        objects = div.find("p", class_="paragraph_exercise").contents
        sub_module_count = objects[1].text.split('.')[1]
        if int(sub_module_count) < int(from_task_count):
            continue
        if to_task_count != 'inf' and int(sub_module_count) > int(to_task_count):
            continue

        task_text = ''
        for i, element in enumerate(objects[2:len(objects) - 2], start=2):
            if isinstance(element, str):
                text = clear_nt(element)
            else:
                text = ' ' + clear_nt(element.text) + ' '
            task_text += text
        final_text = wrap_text(task_text).replace(' .', '.').replace(' ,', ',')

        filename = f'{module_count}-{sub_module_count}.py'
        filepath = os.path.join(catalog_name, filename)

        with open(filepath, "w+", encoding="utf-8") as file:
            file.write(f"'''\n{final_text}\n'''\n\n\n")

        print(f"Задача сохранена в файл: {filepath}")
else:
    print(f"Ошибка при получении страницы: {response.status_code}")
