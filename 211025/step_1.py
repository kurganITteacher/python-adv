a = (1, [1, 2], 'hello')
# a = (1, [1, 2] + [3], 'hello')
a[1] += [3]


def __iadd__(self, other):
    raise TypeError("'tuple' object does not support item assignment")


def __iadd__(self, other):
    self.val += other.val
    return self


def __add__(self, other):
    return self.val + other.val

a[1].append(3)
# print(a)
