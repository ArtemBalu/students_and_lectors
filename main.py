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
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self. grades_from_students = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)


APetrov = Student('Anton', 'Petrov', 'Bunny')
DKuplionv = Lecturer('Dmitry', 'Kuplinov')
LSmirnova = Reviewer('Lilia', 'Smirnova')

APetrov.courses_in_progress.append('123')
DKuplionv.courses_attached.append('123')
LSmirnova.courses_attached.append('123')

print(APetrov.rate_lecturer(DKuplionv, '123', 6))
print('Оценки лектора', DKuplionv.grades_from_students)
print()

print(APetrov.rate_lecturer(DKuplionv, '123', 10))
print('Оценки лектора', DKuplionv.grades_from_students)
print()

print(APetrov.rate_lecturer(DKuplionv, '123', 11))
print('Оценки лектора', DKuplionv.grades_from_students)
print()

print(APetrov.rate_lecturer(LSmirnova, '123', 6))
print()

LSmirnova.rate_hw(APetrov, '123', 4)
print('Оценки Антона', APetrov.grades)