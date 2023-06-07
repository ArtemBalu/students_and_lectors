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
    
    def better_student (self, student1):
        b_student = []
        if isinstance(student1, Student):
            if student1.__average_mark__() < self.__average_mark__():
                b_student = ['Более высокую успеваемость имеет студент', self.name, self.surname]
            elif self.__average_mark__() < student1.__average_mark__():
                b_student = ['Более высокую успеваемость имеет студент', student1.name, student1.surname]
            else:
                b_student = ['Студенты имеют одинаковую успеваемость']
        else:
            b_student = ['Ошибка: один или оба студента не найдены!']
        return " ".join(b_student)
    
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
    
    def better_lecturer (self, lecturer1):
        b_lecturer = []
        if isinstance(lecturer1, Lecturer):
            if lecturer1.__average_mark__() < self.__average_mark__():
                b_lecturer = ['Более высокий рейтинг имеет лектор', self.name, self.surname]
            elif self.__average_mark__() < lecturer1.__average_mark__():
                b_lecturer = ['Более высокий рейтинг имеет лектор', lecturer1.name, lecturer1.surname]
            else:
                b_lecturer = ['У лекторов одинаковый рейтинг']
        else:
            b_lecturer = ['Ошибка: один или оба лектора не найдены!']
        return " ".join(b_lecturer)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка: такого студента не существует, или он не обучается на данном курсе, или курс не закреплен за проверяющим!'
        
    def __str__(self):
        return f"Имя: {self.name}\n"\
               f"Фамилия: {self.surname}\n"

def student_average_course_mark (students_list, course_name):
    import statistics
    marks = []
    sacm = []
    flag = False   # флаг для отлова отсутствия курса в списке
    for student in students_list:
        if isinstance(student, Student):
            if course_name in student.courses_in_progress:
                marks += student.grades[course_name]
                sacm = [f'Средняя оценка за домашние задания на курсе {course_name}: {statistics.mean(marks)}']
                flag = True
            else:
                continue
        else:
            sacm = ['Ошибка: один или несколько людей в списке не являются студентами!']
            flag = True
            break
    if flag == False:
        sacm = [f'{course_name}: нет такого курса!']
    return sacm[0]

def lecturer_average_course_mark (lecturers_list, course_name):
    import statistics
    marks = []
    lacm = []
    flag = False   # флаг для отлова отсутствия курса в списке
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer):
            if course_name in lecturer.courses_attached:
                marks += lecturer.grades_from_students[course_name]
                lacm = [f'Средняя оценка за проведенные лекции на курсе {course_name}: {statistics.mean(marks)}']
                flag = True
            else:
                continue
        else:
            lacm = ['Ошибка: один или несколько людей в списке не являются лекторами!']
            flag = True
            break
    if flag == False:
        lacm = [f'{course_name}: нет такого курса!']
    return lacm[0]

# создадим списки студентов и лекторов, создадим по два экземпляра каждого класса (не считая Mentor) и вызовем методы
students = []
lecturers = []

APetrov = Student('Антон', 'Петров', 'мужской')
MBorisova = Student ('Мария', 'Борисова', 'женский')
students += [APetrov, MBorisova]

GFokin = Lecturer('Георгий', 'Фокин')
VKarpov = Lecturer('Виктор', 'Карпов')
lecturers += [GFokin, VKarpov]

LSmirnova = Reviewer('Лилия', 'Смирнова')
NSimonov = Reviewer('Николай', 'Симонов')

APetrov.courses_in_progress += ['Математика', 'Русский язык', 'Основы Python']
MBorisova.courses_in_progress += ['Литература', 'История']

APetrov.finished_courses += ['Английский язык', 'Экономика']
MBorisova.finished_courses += ['Физика', 'Химия']

GFokin.courses_attached += ['Математика', 'Физика']
VKarpov.courses_attached += ['Русский язык', 'Литература']
LSmirnova.courses_attached += ['История', 'Экономика']
NSimonov.courses_attached += ['Английский язык', 'Химия', 'Основы Python']

APetrov.rate_lecturer(GFokin, 'Математика', 8)   # без ошибок, по два вызова для подсчета средней оценки у лекторов
APetrov.rate_lecturer(GFokin, 'Математика', 6)
MBorisova.rate_lecturer(VKarpov, 'Литература', 10)
MBorisova.rate_lecturer(VKarpov, 'Литература', 3)

print(APetrov.rate_lecturer(GFokin, 'Русский язык', 5))   # предмет не закреплен за лектором, выведем ошибку на экран
print(APetrov.rate_lecturer(VKarpov, 'Литература', 6))   # студент не обучается на этом курсе, выведем ошибку на экран
print(APetrov.rate_lecturer(NSimonov, 'Литература', 6))   # попробуем оценить экземпляр Reviewer

LSmirnova.rate_hw(MBorisova, 'История', 5)   # без ошибок, по два вызова для подсчета средней оценки у студентов
LSmirnova.rate_hw(MBorisova, 'История', 3)
NSimonov.rate_hw(APetrov, 'Основы Python', 2)
NSimonov.rate_hw(APetrov, 'Основы Python', 4)

print(LSmirnova.rate_hw(APetrov, 'Русский язык', 5))   # предмет не закреплен за лектором, выведем ошибку на экран
print(NSimonov.rate_hw(MBorisova, 'Основы Python', 6))   # студент не обучается на этом курсе, выведем ошибку на экран
print(NSimonov.rate_hw(GFokin, 'Основы Python', 6))   # попробуем поставить оценку преподавателем другому преподавателю

print(APetrov.better_student(MBorisova))   # без ошибок
print(APetrov.better_student(NSimonov))   # сравним студента и преподавателя

print(GFokin.better_lecturer(VKarpov))   # без ошибок
print(GFokin.better_lecturer(MBorisova))   # сравним студента и преподавателя

print(student_average_course_mark (students, 'История'))   # без ошибок
print(student_average_course_mark (students, 'Информатика'))   # нет такого курса
print(student_average_course_mark (lecturers, 'История'))   # попытаемся узнать оценки преподавателей

print(lecturer_average_course_mark (lecturers, 'Математика'))   # без ошибок
print(lecturer_average_course_mark (lecturers, 'Физическая культура'))   # нет такого курса
print(lecturer_average_course_mark (students, 'Математика'))   # попытаемся узнать оценки студентов