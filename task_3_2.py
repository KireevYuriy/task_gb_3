print('Вас приветствует программа "Переводчик числительных".\nТребуется ввести число от 0 до десяти на русском или английском и вы получите его перевод.')
translator_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }


def num_translete(word, translate_dict):
    """Функция проверки вхождения введенного слова в словарь и возвращения перевода слова"""
    for item in translate_dict.items():
        key, val = item
        if word == key:
            return val
        elif word == val:
            return key


def num_translate_adv(word, translate_dict):
    """Функция проверки заглавной или строчной первой буквы введенного слова"""
    if ord(word[0]) >= 65 and ord(word[0]) <= 96 or ord(word[0]) >= 1040 and ord(word[0]) <= 1071:
        result = str(num_translete(word.lower(), translate_dict))
        return result.capitalize()
    elif ord(word[0]) >= 97 and ord(word[0]) <= 129 or ord(word[0]) >= 1072 and ord(word[0]) <= 1104:
        return num_translete(word, translate_dict)
    else:
        return print('Вы не ввели слово!')


number = input('Введите слово числительное от 0 до 10: ')
print(f'Ваше слово: {number} -> {num_translate_adv(number, translator_dict)}')
