# 2 (3 балла)
# Используйте replace, чтобы очистить строку poem от знаков препинания, приведите строку к нижнему регистру
# и посчитайте количество различных слов в poem.

poem = """5 little piges.
This little pig went to market,
This little pig stayed at home,
This little pig had roast beef,
And this little pig had none,
This little pig said, "Wee, wee, wee"!
I can't find my way home."""

format_poem = poem.replace('.', '').replace(',', '').replace('\"', '').replace('!', '').lower()
print(format_poem)
li = format_poem.replace('\n', ' ').split(' ')
counter = []
for element in li:
    if element not in counter:
        counter.append(element)

print('Количество различных слов = ', len(counter))
