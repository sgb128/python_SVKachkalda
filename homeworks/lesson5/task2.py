f_file = open('task1.py', 'r', encoding='UTF-8')
v_count_words = dict(enumerate([len(words_count.split()) for words_count in f_file.readlines()], 1))
print('Количество строк: ' + str(len(v_count_words)))
print('Количество слов в строках: ' + str(v_count_words))