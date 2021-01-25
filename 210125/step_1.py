import timeit

name = 'иван'
# заглавная первая буква, а-я,
# dict, set - hash table

alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet.add('ё')

# alphabet_2 = [chr(el) for el in range(ord('а'), ord('я') + 1)]
# alphabet_3 = {chr(el): el for el in range(ord('а'), ord('я') + 1)}
#
# print(type(alphabet), type(alphabet_2), type(alphabet_3))
#
# print('z' in alphabet, 'г' in alphabet)  # O(1)
# print('z' in alphabet_2, 'г' in alphabet_2)  # O(n)
# print('z' in alphabet_3, 'г' in alphabet_3)  # O(1)
#
# print(alphabet)
# print(alphabet_2)
# print(alphabet_3.keys())
#
# set_1 = {'а', 'б', 'в', 'в'}
# set_2 = {'а', 'б'}
#
# print(set_1)
# print(set_2 - set_1)
# print(set_1 - set_2)


to_measure_1 = '''
# name = 'иван'
# alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
# alphabet.add('ё')
is_valid = not set(name) - alphabet
# print(is_valid)
'''

to_measure_2 = '''
# name = 'иван'
# alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
# alphabet.add('ё')
is_valid = True
for letter in name:
    if letter not in alphabet:
        is_valid = False
        break
# print(is_valid)
'''

print(timeit.timeit(to_measure_1, number=1000000, globals={'alphabet': alphabet, 'name': name}))
print(timeit.timeit(to_measure_2, number=1000000, globals={'alphabet': alphabet, 'name': name}))

import time

start = time.perf_counter()
for _ in range(1000000):
    is_valid = not set(name) - alphabet
print(time.perf_counter() - start)

start = time.perf_counter()
for _ in range(1000000):
    is_valid = True
    for letter in name:
        if letter not in alphabet:
            is_valid = False
            break
print(time.perf_counter() - start)
