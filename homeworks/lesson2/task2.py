v_list = []
vn_count = int(input('Введите количество элементов в списке:'))
while vn_count:
    v_list.append(input('Введите элемент списка:'))
    vn_count -= 1

# вот так не работает, почему?
#for item in v_list_1:
#    v_list_1[v_list_1.index(item)], v_list_1[v_list_1.index(item)-1] = v_list_1[v_list_1.index(item)]-1, v_list_1[v_list_1.index(item)]

print(v_list)
v_iterator = 0
for v_iterator in list(range(0, len(v_list) ) ):
    if v_iterator % 2  == 0 and v_iterator + 1 < len(v_list):
        v_list[v_iterator], v_list[v_iterator + 1] = v_list[v_iterator + 1], v_list[v_iterator]
print(v_list)
