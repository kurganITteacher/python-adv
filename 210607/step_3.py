# класс для студентов
# * имя
# * дата рождения
# * адрес
#
# класс учебной группы (композиция)
# * название
# * студенты
# * методы для добавления, удаления и просмотра студентов группы


class Student:
    def __init__(self, name, birth_date, address):
        self.name = name
        self.birth_date = birth_date
        self.address = address


class TeachGroup:
    def __init__(self, name):
        self.name = name
        self.students = []
        # self.students = {}

    def add(self, student):
        self.students.append(student)

    def remove(self, student):
        if student in self.students:
            self.students.remove(student)

    def show(self):
        print(self.name, self.students)


student_1 = Student('Иванов Иван Иванович', '15.05.2002', 'г.Курган, центр')
student_2 = Student('Сергеев Сергей Сергеевич', '04.11.2003', 'г.Курган, центр')
group_1 = TeachGroup('ИТ-33')
group_1.add(student_1)
group_1.add(student_2)
# print(group_1.show())
# group_1.show()
# group_1.remove(student_2)
# group_1.show()

for el in group_1.students:
    print(el.birth_date)

del group_1

print(student_1)
