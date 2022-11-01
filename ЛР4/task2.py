
def sort(string):  # Здесь я сначала добавил сортировку, как в main_str, но она не бьется с "Expected", поэтому убрал :)
    list_ = string.split()
    new_string = "".join(list_)
    new_string = new_string.lower()
    modified_str = ""
    for i in new_string:
        if i.isalpha():
           modified_str += i
    return modified_str


def symbol_char(string):
    sorted_string = sort(string)
    char_ = {

    }
    for i in sorted_string:
        char_[i] = 0
    for j in sorted_string:
            char_[j] += 1
    return char_


def percent_char(string):
    char_ = symbol_char(string)
    for i in char_:
        char_[i] = char_[i] * 100 / len(sort(string))
        char_[i] = round(char_[i], 2)
    return char_  #возвращает словарь, где значение ключа - количество процентов (не долей от 100)


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(symbol_char(main_str))
print(percent_char(main_str))