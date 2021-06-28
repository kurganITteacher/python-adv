# DRY
students = ['Иван', 'Мария', 'Сергей']

# for student in students:
#     print(student)

idx = 1
for student in students:
    print(idx, student)
    idx += 1

for idx, student in enumerate(students, 1):
    print(idx, student)
