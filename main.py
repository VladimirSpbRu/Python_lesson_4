# Функция, создающая из списка имён и целого числа N новый список имён длиной N элементов
import random
def function_1 (local_source_list, local_list_length):
    '''
    :param local_source_list: исходный список имен
    :param local_list_length: длина выходного списка имен
    :return: возвращает список имен длиной local_list_length, рандомно набранный из исходного списка имен
    '''
    long_list = []
    for i in range (1, local_list_length+1):
        long_list.append(random.choice(local_source_list))
    return long_list

# Функция вывода самого частого имени из списка
def function_2 (local_long_list, local_source_list):
    text_dict = {}
    for list_element_number in range(len(local_source_list)):
        number_of_repeats = 0
        for i in range(len(local_long_list)):
            if local_long_list[i] == local_source_list[list_element_number]:
                number_of_repeats+= 1
        text_dict[local_source_list[list_element_number]] = number_of_repeats

    aux_list = list(text_dict.items())
    aux_list.sort(key = lambda i: i[1])
    one_more_aux_list = list(aux_list[len(aux_list) - 1])
    most_frequent_name = one_more_aux_list[0]
    return most_frequent_name

# Функция вывода самой редкой буквы, с которой начинаются имена из списка
def function_3 (local_long_list):
    list_of_letters = list(map(lambda x: x[0], local_long_list))
    unique_letters_list = list(set(list_of_letters))
    letters_dict = {}
    for list_element_number in range(len(unique_letters_list)):
        number_of_repeats = 0
        for i in range(len(list_of_letters)):
            if list_of_letters[i] == unique_letters_list[list_element_number]:
                number_of_repeats+= 1
        letters_dict[unique_letters_list[list_element_number]] = number_of_repeats

    aux_list = list(letters_dict.items())
    aux_list.sort(key=lambda i: i[1])
    one_more_aux_list = list(aux_list[0])
    rearest_letter = one_more_aux_list[0]
    return rearest_letter

# Ввод исходных данных
source_text_str = input('Введите несколько имён через пробел: ')
list_length = int(input('Введите количество имен в итоговом списке: '))
source_list = source_text_str.split()

# Исполнение ранее написанных функций
long_list = function_1(source_list, list_length)
print('Преобразованный (случайный) список длиной', list_length, 'имён:', long_list)
most_frequent_name = function_2(long_list, source_list)
print('Самое частое имя в длинном списке:', most_frequent_name)
rearest_letter = function_3(long_list)
print('Самая редкая буква начала имени в длинном списке:', rearest_letter)