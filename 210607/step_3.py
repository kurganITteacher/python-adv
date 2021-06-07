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
