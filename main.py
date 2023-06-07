class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка: такого лектора не существует, или он не преподает на данном курсе, или студент не обучается на данном курсе, или некорректная оценка!'

    def __average_mark__(self):
        import statistics
        average_for_subj = []
        for value in self.grades.values():
            average_for_subj.append(statistics.mean(value))
        return statistics.mean(average_for_subj)

    def __str__(self):
        return f"Имя: {self.name}\n"\
               f"Фамилия: {self.surname}\n"\
               f"Средняя оценка за домашние задания: {self.__average_mark__()}\n"\
               f"Курсы в процессе изучения: {', '.join (self.courses_in_progress)}\n"\
               f"Завершенные курсы: {', '.join (self.finished_courses)}\n"
    
    def better_student (self, student1, student2):
        b_student = []
        if isinstance(student1, Student) and isinstance(student2, Student):
            if student1.__average_mark__() < student2.__average_mark__():
                b_student = [student2.name, student2.surname, student2.__average_mark__()]
            elif student2.__average_mark__() < student1.__average_mark__():
                b_student = [student1.name, student1.surname, student1.__average_mark__()]
            else:
                b_student = ['Студенты имеют одинаковую успеваемость']
        else:
            b_student = ['Ошибка: один или оба студента не найдены!']
        return ','.join(b_student)
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self. grades_from_students = {}

    def __average_mark__(self):
        import statistics
        average_for_subj = []
        for value in self.grades_from_students.values():
            average_for_subj.append(statistics.mean(value))
        return statistics.mean(average_for_subj)

    def __str__(self):
        return f"Имя: {self.name}\n"\
               f"Фамилия: {self.surname}\n"\
               f"Средняя оценка за лекции: {self.__average_mark__()}\n"
    
    def better_lecturer (self, lecturer1, lecturer2):
        b_lecturer = []
        if isinstance(lecturer1, Lecturer) and isinstance(lecturer2, Lecturer):
            if lecturer1.__average_mark__() < lecturer2.__average_mark__():
                b_lecturer = [lecturer2.name, lecturer2.surname, lecturer2.__average_mark__()]
            elif lecturer2.__average_mark__() < lecturer1.__average_mark__():
                b_lecturer = [lecturer1.name, lecturer1.surname, lecturer1.__average_mark__()]
            else:
                b_lecturer = ['У лекторов одинаковый рейтинг']
        else:
            b_lecturer = ['Ошибка: один или оба лектора не найдены!']
        return ','.join(b_lecturer)       

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\n"\
               f"Фамилия: {self.surname}\n"


APetrov = Student('Anton', 'Petrov', 'Bunny')
DKuplionv = Lecturer('Dmitry', 'Kuplinov')
LSmirnova = Reviewer('Lilia', 'Smirnova')

APetrov.courses_in_progress.append('Русский язык')
APetrov.courses_in_progress.append('Математика')
APetrov.courses_in_progress.append('Литература')

APetrov.finished_courses.append('Английский язык')

DKuplionv.courses_attached.append('Русский язык')
DKuplionv.courses_attached.append('Математика')
DKuplionv.courses_attached.append('Литература')

LSmirnova.courses_attached.append('Русский язык')
LSmirnova.courses_attached.append('Математика')
LSmirnova.courses_attached.append('Литература')

APetrov.rate_lecturer(DKuplionv, 'Математика', 6)
# print('Оценки лектора', DKuplionv.grades_from_students)
# print()

APetrov.rate_lecturer(DKuplionv, 'Русский язык', 10)
# print('Оценки лектора', DKuplionv.grades_from_students)
# print()

APetrov.rate_lecturer(DKuplionv, 'Литература', 11)
# print('Оценки лектора', DKuplionv.grades_from_students)
# print()

APetrov.rate_lecturer(LSmirnova, 'Математика', 6)
# print()

LSmirnova.rate_hw(APetrov, 'Математика', 4)
LSmirnova.rate_hw(APetrov, 'Математика', 2)
LSmirnova.rate_hw(APetrov, 'Математика', 3)
LSmirnova.rate_hw(APetrov, 'Математика', 4)
# print('Оценки Антона', APetrov.grades)

print(APetrov)
print(DKuplionv)
print(LSmirnova)