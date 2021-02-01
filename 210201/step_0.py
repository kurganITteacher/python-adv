# https://github.com/H0oxy/-python-adv/blob/main/21.01.25/hw.py
"""
1. Написать валидацию даты на чистом python (без re)
2, 3. Написать валидатор для вещественных чисел: 1.32 или 1,32 (с re и на чистом python)
"""
import re

# RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^[\d]{1,}[.|,][\d]+$')
# RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^[\d]{1,}[.|,][0-9]+$')
# RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^\d{1,}[.|,]\d+$')
# RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^\d+[.|,]\d+$')
# RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^\d+[.,]?\d+$')
# RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^\d+[.,]?\d*$')
# RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^[.,]?(\d+)$')
# RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^\d+([.,]\d+)*$')
RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^\d+([.,]\d+)?$')


def number_is_valid(number):
    return RE_REAL_NUMBERS_VALIDATOR.match(number)


assert not number_is_valid('1.d2')
assert not number_is_valid('d.32')
# assert not number_is_valid('132')  # ?
assert not number_is_valid('abc')  # ?
assert number_is_valid('132')  # ?
assert number_is_valid('13')  # ?
assert number_is_valid('1')  # ?
assert number_is_valid('1.32')
assert not number_is_valid('1.32.32')
assert not number_is_valid('1.')
assert not number_is_valid('.32')
assert number_is_valid('1,32')
assert number_is_valid('10,32')
assert not number_is_valid('1|32') # ???


