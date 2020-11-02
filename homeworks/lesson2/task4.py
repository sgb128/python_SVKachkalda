vs_string = input('Введите произвольную строку:')
l_list = []
v_space_count = vs_string.count(' ')
v_space_index = -1

for v_index in list(range(0, len(vs_string))):
    v_right_decr = 0
    if vs_string[v_index] == ' ':
        if v_index > 0 and vs_string[v_space_index + 1:v_index] != ' ' and len(vs_string[v_space_index + 1:v_index]) > 0:
            if v_index - v_space_index - 1 > 10:
                v_right_decr = v_index - v_space_index - 1 - 10
            else:
                v_right_decr = 0
            l_list.append(vs_string[v_space_index + 1:v_index - v_right_decr])
        v_space_index = v_index

if v_space_index != len(vs_string) and vs_string[v_space_index + 1:len(vs_string)] != ' ' and len(vs_string[v_space_index + 1:len(vs_string)]) > 0:
    if len(vs_string) - v_space_index - 1 > 10:
        v_right_decr = len(vs_string) - v_space_index - 1 - 10
    else:
        v_right_decr = 0
    l_list.append(vs_string[v_space_index + 1:len(vs_string) - v_right_decr])

for item in l_list:
    print(str(l_list.index(item) + 1) + '. ' + item)