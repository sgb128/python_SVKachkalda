def f_initcap(p_word: str):
    """
    f_initcap возвращает новую строку начинающуюся с заглавной буквы
    :param p_word: строка начинающаяся с буквы
    :return: строка первая буква которой заглавная
    """
    s_result = ''
    if len(p_word) > 0:
        if p_word[0].islower():
            s_result = p_word[0].upper() + p_word[1:]
        else:
            s_result = p_word[:]
    return s_result

def f_initwords(p_string: str):
    """
    f_initwords возвращает строку все слова в которой начинаются с заглавной буквы
    :param p_string: строка
    :return: строка
    """
    v_result = ''
    for i_item in p_string.split(' '):
        v_result += f_initcap(i_item) + ' '
    return v_result[:-1]

print(f_initwords('word  word   word word '))
