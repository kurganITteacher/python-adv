def valid_name(txt):
    return txt.istitle()


students = ['иван', 'Мария', 'Сергей']
students_upd = (el for el in students if valid_name(el))  # memory O(1)
print(students_upd)
# print(students_upd[1])
# print(next(students_upd))
# print(next(students_upd))

students_upd_2 = filter(valid_name, students)  # memory O(1)
print(students_upd_2)
# print(students_upd_2[1])
# print(next(students_upd_2))
# print(next(students_upd_2))
