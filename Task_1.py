# 1 (1 балл)
# На вход вам приходит строка, в которой буква h встречается минимум два раза.
# Выведите эту строку без первого и последнего вхождение буквы h, а также без всех символов, находящихся между ними.

line = 'AAAhDDDhCCChFFF'
search_start = line.find('h')
search_end = line.rfind('h')
div = line[search_start:search_end+1]
format_line = line.replace(div, '')
print(format_line)
