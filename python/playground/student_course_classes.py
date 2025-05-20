#!/usr/bin/python3

"""
Difinition of a class Student
"""
class Student:
    """
    constructure method called when a new Student object is created.
    """
    def __init__(self, name, age, grade):
        self.name = name        # stores the student's name in the instance
        self.age = age          # stores the student's age
        self.grade = grade      # stores student's grade 0 - 100

    # method to return student grade
    def get_grade(self):
        return self.grade   # return the grade stored in the instance

"""
Difinition of a class Course
"""
class Course:
    """
    constructure method called when a new Course object is created
    """
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []      # initialized new empty array to hold enrolled student object

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True         # return true if student was added
        
        return False            # return if course is full

    def get_average_grade(self):
        value = 0
        
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)   # return the average grade


student1 = Student('Rudra', 20, 98)
student2 = Student('Mamata', 20, 99)
student3 = Student('Max', 40, 50)
student4 = Student('Rolex', 40, 50)

course = Course('Science', 2)

course.add_student(student1)
course.add_student(student2)

""" Note: If you try to add student 3 you will get index out of range error """
print(course.add_student(student3))
print(course.add_student(student4))

print(student1.name)
print(course.students[1].name)
print(course.get_average_grade())
