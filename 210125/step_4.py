import re
import time

name = 'иван'
# заглавная первая буква, а-я,
# dict, set - hash table

RE_NAME_VALIDATOR = re.compile(r'^[А-ЯЁ][а-яё]+$')  # 0, 9999999999

assert not RE_NAME_VALIDATOR.match('иван')
# print(RE_NAME_VALIDATOR.match('иван'))
# print(RE_NAME_VALIDATOR.match('Иван'), RE_NAME_VALIDATOR.match('Иван').group(0))
# print(RE_NAME_VALIDATOR.match('Иван '))
# print(RE_NAME_VALIDATOR.fullmatch('Иван '))


alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet.add('ё')

start = time.perf_counter()
for _ in range(1000000):
    is_valid = not set(name) - alphabet
print(time.perf_counter() - start)

start = time.perf_counter()
for _ in range(1000000):
    is_valid_2 = True
    for letter in name:
        if letter not in alphabet:
            is_valid_2 = False
            break
print(time.perf_counter() - start)

start = time.perf_counter()
for _ in range(1000000):
    is_valid_3 = RE_NAME_VALIDATOR.match(name)
print(time.perf_counter() - start)

import timeit

to_measure_1 = '''
is_valid = not set(name) - alphabet
'''

to_measure_2 = '''
is_valid = True
for letter in name:
    if letter not in alphabet:
        is_valid = False
        break
'''

to_measure_3 = '''
is_valid = RE_NAME_VALIDATOR.match(name)
'''

print(timeit.timeit(to_measure_1, globals={'alphabet': alphabet, 'name': name}))
print(timeit.timeit(to_measure_2, globals={'alphabet': alphabet, 'name': name}))
print(timeit.timeit(to_measure_3, globals={'RE_NAME_VALIDATOR': RE_NAME_VALIDATOR, 'name': name}))
