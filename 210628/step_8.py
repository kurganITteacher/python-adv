def valid_name(txt):
    return txt.istitle()


students = ['иван', 'Мария', 'Сергей']
students_upd = []
for el in students:
    if valid_name(el):
        students_upd.append(el)
print(students_upd)

students_upd_2 = list(filter(valid_name, students))
print(students_upd_2)
