# import random

def str_to_int(func):
    def inner(*args):
        return func(*map(int, args))

    return inner


def str_to_float(func):
    def inner(*args):
        return func(*map(float, args))

    return inner


# def my_sum(a, b):
#     return a + b


# @str_to_int
@str_to_float
def nums_sum(*nums):
    return sum(nums)
    # return sum(map(int, nums))
    # return sum(map(float, nums))


print(nums_sum(2, 3))
print(nums_sum(2.3, 3.5))
# a = input()
# b = input()
# print(my_sum(a, b))
print(nums_sum('2', '3'))
print(nums_sum('2.3', '3.5'))
