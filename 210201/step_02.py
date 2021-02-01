# https://github.com/PlagueEvgeny/python/blob/main/lesson_210125/homework_1.py
numbers = {chr(el) for el in range(ord('0'), ord('9') + 1)}
numbers.update(['/', '-', '.'])

required_numbers = {'/'}
required_numbers_1 = {'-'}
required_numbers_2 = {'.'}
_required_numbers = [{'/'}, {'-'}, {'.'}]
possible_splitters = ['/', '-', '.']
# b = 8


def data_is_valid(raw_data):
    # global b
    # print(b)
    # b += 1
    # global data1  # VERY NOT GOOD
    # data_is_set = set(data)  # data_is_set?
    data_as_set = set(raw_data)  # data_is_set?
    # data_as_set - numbers ? 01.02.2021 -> {'0', '1', '2', '.'} || {'0', '1', '2', ..., '/', ',', '-', '.'}

    # if not data or data_as_set - numbers or required_numbers - data_as_set:
    #     if not data or data_as_set - numbers or required_numbers_1 - data_as_set:
    #         if not data or data_as_set - numbers or required_numbers_2 - data_as_set:
    #             return False

    if not raw_data or data_as_set - numbers:
        if required_numbers - data_as_set or required_numbers_1 - data_as_set or \
                required_numbers_2 - data_as_set:
            return False

    # if not data or data_as_set - numbers or any([el - data_as_set for el in _required_numbers]):
    #     return False

    # for data1 in required_numbers:
    #     count = data.count(data1)
    #     if count != 2:
    #         for data1 in required_numbers_1:
    #             count = data.count(data1)
    #             if count != 2:
    #                 for data1 in required_numbers_2:
    #                     count = data.count(data1)
    #                     if count != 2:
    #                         return False
    #
    # splitter_is_ok = False
    # for splitter in possible_splitters:
    #     if data.count(splitter) == 2:
    #         splitter_is_ok = True
    #         break
    # if not splitter_is_ok:
    #     return False

    for splitter in possible_splitters:
        if raw_data.count(splitter) == 2:
            break
    else:
        return False

    day, month, year = raw_data.split(splitter)
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False
    return True


assert data_is_valid('25.01.2021')
assert data_is_valid('25/01/2021')
assert data_is_valid('25-01-2021')
assert not data_is_valid('5.01.2021')
assert not data_is_valid('05.01.21')
assert not data_is_valid('05,01,2021')
assert not data_is_valid('05.01.21/')
assert not data_is_valid('05,01,,2021')

# print(b)
