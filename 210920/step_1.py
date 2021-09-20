def my_sum(*args):
    # *args = 1, 2, 3
    print(type(args))
    print(args)
    return sum(args)


def my_sum_2(args):
    # args = [1, 2, 3]
    return sum(args)


print(my_sum(1, 2, 3))  # a
# my_sum([1, 2, 3])  # b

# my_sum_2(1, 2, 3)  # c
print(my_sum_2([1, 2, 3]))  # d

_, *args = 0, 1, 2, 3
args_2 = [1, 2, 3]
print(args)
print(args_2)
