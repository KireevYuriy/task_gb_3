names = ['Игорь', 'Александр', 'Инна', 'Владимир', 'Анна', 'Иван', 'Данила', 'Роман', 'Анастасия', 'Дарья',
         'Иннокентий']
letter_names = {}


def thesaurus(letter_key, list_names):
    """
    Функция проверяет первую букву имени со всеми именами, если имен несколько, формирует список из этих имен,
    если имя одно, то список из одного имени. Функция возвращает букву и список имен на эту букву.
    """
    same_name = []
    for check_name in list_names:
        if letter_key == check_name[0]:
            same_name.append(check_name)
    return letter_key, same_name


for name in names:
    key, val = thesaurus(name[0], names)
    letter_names.setdefault(key, val)
letter_names = dict(sorted(letter_names.items()))
for key, val in letter_names.items():
    print('{0}: {1}'.format(key, val))