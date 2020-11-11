import os
import random as rand
# путь к файлу
p_data = os.path.join(os.path.dirname(__file__), 'task5.txt')

l_list = [rand.randint(1, 1000) for _ in range(20)]
with open(p_data, 'w', encoding='UTF-8') as f_file:
    f_file.write(str(' '.join(map(str, l_list))))

with open(p_data, 'r', encoding='UTF-8') as f_file:
    result = sum(map(int, f_file.readline().split()))
print(result)
