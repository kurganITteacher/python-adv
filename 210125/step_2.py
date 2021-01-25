# заглавная первая буква, а-я,
# dict, set - hash table

alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
# alphabet.add('ё')
alphabet.update(['ё', '-'])


# Анна-Виктория


def name_is_valid(name):
    if not name or set(name.lower()) - alphabet:  # case insensitive
        return False
    # if '-' in name:
    #     for _name in name.split('-'):
    #         if not _name.istitle():
    #             return False
    #     return True
    return name.istitle()


# print(name_is_valid('иван'))
# print(name_is_valid('Иван'))
# print(name_is_valid('Анна-Виктория'))

assert not name_is_valid('иван'), 'иван is valid name?'
assert name_is_valid('Иван'), 'Иван is not valid name?'
assert name_is_valid('Анна-Виктория'), 'Иван is not valid name?'
