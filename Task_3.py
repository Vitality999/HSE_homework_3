# 3 (3 балла)
# Скачайте файл с распространенными паролями:
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-500.txt
# Откройте файл в Питоне с помощью whith. Проитерируйтесь по строкам и проверьте каждый пароль на надежность.
# Будем считать пароль надежным, если в нем минимум 6 символов разного регистра, есть цифры, буквы и другие символы.
# Выведете долю надежных паролей среди всех в файле.
#
# В решении могут помочь методы .isupper() , .isdigit() , .isalpha()

with open('passwords.txt', 'r', encoding='utf-8') as pas:
    count = []
    counter = []
    for line in pas:
        count.append(line)
        if len(line) >= 6:
            counter.append(line.replace('\n', ''))
            for x in counter:
                if x.isalpha() or x.isdigit() or x.islower() or x.isupper():
                    counter.remove(x)
    z = len(counter) / len(count) * 100
    print('Список безопасных паролей:', counter)
    print('Общее количество паролей:', len(count))
    print('Доля безопасных паролей от всего списка:', round(z, 4), '%')


#для выполнения условия, описанного в задаче, добавил 1 запись в список паролей, иначе ни один из паролей небезопасен.