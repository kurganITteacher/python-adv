# заглавная первая буква, а-я,
# dict, set - hash table

alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet.add('ё')


def name_is_valid(name):
    if not name or set(name.lower()) - alphabet:  # case insensitive
        return False
    return name.istitle()


print(name_is_valid('иван'))
print(name_is_valid('Иван'))
