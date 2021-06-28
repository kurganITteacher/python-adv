# mutable
# immutable
workers = ['Иван', 'Мария']
print(id(workers), workers)
workers[0] = 'Сергей'  # O(1)
print(id(workers), workers)

# list vs tuple

# workers = ['Иван', 'Мария', ..., 'Григорий']
# workers.pop(0)  # O(n) -> queue
# workers.pop()  # O(1)
# print(workers[1])  # O(1)

# iterable

