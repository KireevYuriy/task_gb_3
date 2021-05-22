names = ['Инна Пушкарева', 'Игорь Иванов', 'Ирина Пивнева', 'Александр Пушкин', 'Анна Ахматова', 'Иван Орлов',
         'Данила Козлов', 'Роман Истомин']
result_names = {}


def thesaurus_adv(one_person, list_names):
    """Функция разделения элементов списка в алфавитном порядке по первой букве фамилии, а затем имени"""
    temporary_list = []
    into_dict = {}
    separate_name = one_person.split(sep=' ')
    for check_name in list_names:
        name_list = check_name.split(sep=' ')
        if separate_name[1][0] == name_list[1][0]:
            temporary_list.append(check_name)
    for check_name in temporary_list:
        name_dict = {}
        if into_dict.get(check_name[0][0]) is None:
            into_dict.setdefault(check_name[0], check_name)
        else:
            # Не смог додуматься как корректнее добавить элеметы в список
            some_name = [*into_dict.values()]
            some_name.append(check_name)
            name_dict.setdefault(check_name[0][0], some_name)
            into_dict.update(name_dict)
    return separate_name[1][0], dict(sorted(into_dict.items()))


for name in names:
    key, val = thesaurus_adv(name, names)
    result_names.setdefault(key, val)
result_names = dict(sorted(result_names.items()))
print(f'Входной список данных:\n{names}\n')
# Перебор элементов словаря для вывода
for item in result_names.items():
    print(item)
