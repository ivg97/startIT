from django.utils.text import slugify

translit_alphabet = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
    'ы': 'y', 'ь': '', 'э': 'eh', 'ю': 'yu', 'я': 'ya'
}

def translite(value):
    '''
        Транслитерация кирилицы для слага
        Из русского предложение в английское
    '''
    value = str(value).lower()
    return slugify(''.join(translit_alphabet[letter]
                           if letter in translit_alphabet else letter for
                           letter in value))