s_user_input = input('Введите текст:')
f_file = open('task1.txt', 'w', encoding='UTF-8')
while s_user_input:
    f_file.write(s_user_input)
    s_user_input = input('Введите еще текст или оставьте строку пустой и нажмите Ввод для завершения:')
f_file.close()