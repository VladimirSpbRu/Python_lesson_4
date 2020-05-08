# Функция, создающая из списка имён и целого числа N новый список имён длиной N элементов
import random
def dirty_function (local_source_list, local_list_length):
    '''
    :param local_source_list: исходный список имен
    :param local_list_length: длина выходного списка имен
    :return: возвращает список имен длиной local_list_length, рандомно набранный из исходного списка имен
    '''
    long_list = []
    for i in range (1, local_list_length+1):
        long_list.append(random.choice(local_source_list))
    return long_list

# Автотесты к грязной функции (приведенной выше)
def test_dirty_function_1():
    source_list = ['Аня', 'Катя', 'Степа']
    list_length = 7
    if len(dirty_function(source_list, list_length)) == list_length:
        print('Test is passed.')
    else:
        print('Test is failed.')

def test_dirty_function_2():
    source_list = ['Аня', 'Катя', 'Степа']
    list_length = 7
    long_list = dirty_function(source_list, list_length)
    set_list = list(set(long_list))
    error_num = 0
    for el in set_list:
        if el != source_list[0] and el != source_list[1] and el != source_list[2]:
            error_num += 1
    if error_num == 0:
        print('Test is passed.')
    else:
        print('Test is failed.')