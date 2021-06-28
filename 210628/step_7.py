def title(txt):
    return txt[0].upper() + txt[1:]


def show_title(txt):
    print(txt[0].upper() + txt[1:])
    # return None


# msg = 'месяц'
# # print(title(msg))
# # show_title(msg)
# print(show_title(msg))

students = ['иван', 'мария', 'сергей']
students_upd = []
for el in students:
    students_upd.append(title(el))
print(students_upd)

students_upd_2 = list(map(title, students))
print(students_upd_2)
# print(*students_upd_2)
# print(next(students_upd_2))
# print(next(students_upd_2))
# next()
