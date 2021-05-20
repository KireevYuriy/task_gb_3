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


def num_translate(word, translate_dict):
    """Функция проверки вхождения введенного слова в словарь и возвращения перевода слова"""
    for item in translate_dict.items():
        key, val = item
        if word == key:
            return val
        elif word == val:
            return key


number = input('Введите слово числительное от 0 до 10: ')
print(f'Ваше слово: {number} -> {num_translate(number.lower(), translator_dict).capitalize()}')
