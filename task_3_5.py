import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "светлый"]
number_jokes = int(input('Введите колличество генерируемы шуток: '))


def get_jokes(number, list_one, list_two, list_three):
    """
    Функция-генератор шуток из слов полученных из трех заданных списков. Все шутки уникальны, так как слова в них
    не повторяются. .pop с указание индекса не использовался(как и говорили на уроке), делал срез.
    """
    result_jokes_list = []
    for i in range(number):

        if list_one == [] or list_two == [] or list_three == []:
            print('Были использованы все слова из трех списков!')
            return result_jokes_list
        else:
            idx_one = random.randrange(len(list_one))
            idx_two = random.randrange(len(list_two))
            idx_three = random.randrange(len(list_three))
            list_jokes = f'{list_one[idx_one]} {list_two[idx_two]} {list_three[idx_three]}'
            list_one = list_one[:idx_one] + list_one[idx_one + 1:]
            list_two = list_two[:idx_two] + list_two[idx_two + 1:]
            list_three = list_three[:idx_three] + list_three[idx_three + 1:]
            result_jokes_list.append(list_jokes)

    return result_jokes_list


print(get_jokes(number_jokes, nouns, adverbs, adjectives))
