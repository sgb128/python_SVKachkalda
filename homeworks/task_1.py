"""
пределение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
"""
from collections import Counter

A = 'abefe'
A_ = ['a', 'ab', 'abe', 'abef',
      'b', 'be', 'bef', 'befe',
      'e', 'ef', 'efe',
      'f', 'fe']

B = 'abcbc'
B_ = ['a', 'ab', 'abc', 'abcb',
      'b', 'bc', 'bcb', 'bcbc',
      'c', 'cb', 'cbc']

C = 'abracadabra'
C_ = ['a', 'ab', 'abr', 'abra', 'abrac', 'abraca', 'abracad', 'abracada', 'abracadab', 'abracadabr',
      'b', 'br', 'bra', 'brac', 'braca', 'bracad', 'bracada', 'bracadab', 'bracadabr', 'bracadabra',
      'r', 'ra', 'rac', 'raca', 'racad', 'racada', 'racadab', 'racadabr', 'racadabra',
           'ac', 'aca', 'acad', 'acada', 'acadab', 'acadabr', 'acadabra',
      'c', 'ca', 'cad', 'cada', 'cadab', 'cadabr', 'cadabra',
           'ad', 'ada', 'adab', 'adabr', 'adabra',
      'd', 'da', 'dab', 'dabr', 'dabra']

def s_hash(val):
    letter = 26
    hash_ = 0
    size = 10_000
    for index, char in enumerate(val):
        hash_ += (ord(char) - ord('a') + 1 ) * letter ** index
    return hash_ % size


def substr_sum(data):
    spam = Counter()
    for i in range(len(data)+1):
        for j in range(i + 1, len(data)+1):
            if not (not i and j == len(data)):
                spam[s_hash(data[i:j])] += 1
#                print(data[i:j], i, j, spam[hash(data[i:j])])
    return len(spam)


print('Длина проверочного массива A_:', len(A_))
print('Количество подстрок A:', substr_sum(A))
print('Длина проверочного массива B_:', len(B_))
print('Количество подстрок B:', substr_sum(B))
print('Длина проверочного массива C_:', len(C_))
print('Количество подстрок C:', substr_sum(C))

# Не знаю что в итоге надо было сделать. 8 часов потратил на это задание. + Сама постановка задачи ну как бы сказать -
# не совсем понятная. Какой алгоритм должен быть? Для чего использовать хеш-функцию?
# На уроке не было сказано как хеш-функция помогает определить количество уникальных значений в веденных данных
# В общем сдаю как есть. Неправильно - значит неправильно
