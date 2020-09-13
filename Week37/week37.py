import ast
import random as r
import csv
import platform
from faker import Faker
fake = Faker()
if platform.system() == 'Windows':
    newline=''
else:
    newline=None

class Student():

    def __init__(self, student_id, name, gender, data_sheet, image_url):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
        
    def get_avg_grade(self):
        grade_list = self.data_sheet.get_grades_as_list()
        if len(grade_list) == 0:
            return 0
        avg_grade = 0
        for grade in grade_list:
            avg_grade += grade
        return round(avg_grade/len(grade_list))
    
    def show_progression(self):
        ETCS_needed = 150
        ETCS_completed = 0
        for course in self.data_sheet.courses:
            if self.student_id in course.optional_grades:
                if course.optional_grades[self.student_id] >= 2:
                    ETCS_completed += course.ETCS
        completed_per = ETCS_completed / ETCS_needed
        return round(completed_per*100, 2)

    def __str__(self):
        return 'Student {s_id}: {name}, {gender}, {image_url}'.format(s_id=self.student_id, name=self.name, gender=self.gender, image_url=self.image_url)
        
class DataSheet():

    def __init__(self, student_id, courses=[]):
        self.student_id = student_id
        self.courses = courses

    def __str__(self):
        return 'DataSheet {data_sheet}'.format(data_sheet=self.courses)
        
    def __repr__(self):
        return self.__str__()
        
    def get_grades_as_list(self):
        result = []
        for course in self.courses:
            if self.student_id in course.optional_grades:
                result.append(course.optional_grades[self.student_id])
        return result

        
class Course():

    def __init__(self, name, classroom, teacher, ETCS, optional_grades):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.optional_grades = optional_grades

    def __str__(self):
        return 'Course {c_name}, {c_classroom}, {c_teacher}, {c_ETCS}, {c_optional_grades} '.format(c_name=self.name, c_classroom=self.classroom, c_teacher=self.teacher, c_ETCS=self.ETCS, c_optional_grades=self.optional_grades)

    def __repr__(self):
        return self.__str__()



genders = ("Male","Female")
grades = (-3,0,2,4,7,10,12)

#print(fake.name())

def create_random_student(number_of_students):
    course_math = Course("Math", "101", fake.name(), 20, {})
    course_programming = Course("Programming", "102", fake.name(), 20, {})
    course_english = Course("English", "103", fake.name(), 25, {})
    course_physics = Course("Physics", "104", fake.name(), 30, {})
    course_history = Course("History", "105", fake.name(), 10, {})
    courses = [course_math, course_programming, course_english, course_physics, course_history]
    
    student_list = []
    for student_id in range(1,number_of_students+1):
        name = fake.name()
        image_url = name.replace(" ", "") + ".img"
        gender = genders[r.randint(1,len(genders))-1]
        student_courses = []
        for course in courses:
            if r.randint(1,2) == 1:
                student_courses.append(course)
                if r.randint(1,2) == 1:
                    course.optional_grades[student_id] = grades[r.randint(1,len(grades))-1]
        data_sheet = DataSheet(student_id, student_courses)
        new_student = Student(student_id, name, gender, data_sheet, image_url)
        student_list.append(new_student)
    
    # export data to a .csv file
    with open("randomStudents.csv", 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)

        for student in student_list:
            student_courses = []
            student_optional_grades = []
            for course in student.data_sheet.courses:
                student_courses.append([course.name, course.classroom, course.teacher, course.ETCS])
                if student.student_id in course.optional_grades:
                    student_optional_grades.append(course.optional_grades[student.student_id])
                else:
                    student_optional_grades.append("No Grade")
            output_writer.writerow([student.student_id, student.name, student.gender, student_courses, student_optional_grades, student.image_url]) 

create_random_student(10)


student_list = []
course_list = []
with open("randomStudents.csv") as file_object:
    reader = csv.reader(file_object)
    
    print("Normal List:")
    for row in reader:
        student_id = row[0]
        student_name = row[1]
        student_gender = row[2]
        student_courses_info = ast.literal_eval(row[3])
        student_optional_grades = ast.literal_eval(row[4])
        student_image_url = row[5]
        student_courses = []
        #print(id)
        
        for next_course in student_courses_info:
            course_index = student_courses_info.index(next_course)
            new_course = None
            for course in course_list:
                if next_course[0] == course.name:
                    new_course = course
                    break
            if new_course == None:
                new_course = Course(next_course[0], next_course[1], next_course[2], next_course[3], {})
                course_list.append(new_course)
            student_courses.append(new_course)
            if not isinstance(student_optional_grades[course_index], str):
                new_course.optional_grades[student_id] = student_optional_grades[course_index]
                
        student_data_sheet = DataSheet(student_id, student_courses)
        new_student = Student(student_id, student_name, student_gender, student_data_sheet, student_image_url)
        student_list.append(new_student)

        #print("Student:",new_student.name,"Image URL:",student_image_url,"Average Grade:",new_student.get_avg_grade())
        

#print("\nSorted by avg grade")

def student_sort(student):
    return student.get_avg_grade()

student_list.sort(reverse=True, key=student_sort)
    
#for student in student_list:
    #print("Student:",student.name,"Image URL:",student_image_url,"Average Grade:",student.get_avg_grade())


class NotEnoughStudentsException(Exception):
    pass

def progress_sort(s):
    return s.show_progression()

def three_closest_students(s_list):
    try:
        if len(s_list) < 3:
            raise NotEnoughStudentsException()
        s_list.sort(reverse=True, key=progress_sort)
        return list([s_list[0], s_list[1], s_list[2]])
    except NotEnoughStudentsException:
        print('ERROR: Not enough students in list!')
    
#1
print("3 closes on ETCS points")
three_closest = (three_closest_students(student_list))
student_courses = []
student_optional_grades = []
for student in three_closest:
    for course in student.data_sheet.courses:
        student_courses.append([course.name, course.classroom, course.teacher, course.ETCS])
        if student.student_id in course.optional_grades:
            student_optional_grades.append(course.optional_grades[student.student_id])
        else:
            student_optional_grades.append("No Grade")
    print([student.student_id, student.name, student.gender, student_courses, student_optional_grades, student.image_url])
    #print(student.name, student.data_sheet)


    
#2
#print("\nExpecting error as list is empty")
#three_closest = three_closest_students([])

#3
def three_closest_students_too_file(s_list):
    
    with open("TopThreeStudents.csv", 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        try:
            if len(s_list) < 3:
                raise NotEnoughStudentsException()
            #s_list.sort(key=progress_sort)
            three_closest = three_closest_students(s_list)
            for s in three_closest:
                output_writer.writerow([s.student_id, s.name, s.gender, s.data_sheet, s.image_url])
                    
        except NotEnoughStudentsException:
            output_writer.writerow(['ERROR: Not enough students in list!'])
            
#three_closest_students_too_file(student_list)