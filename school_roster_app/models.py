
import json
import sys
import subprocess
import os

class Person:

    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

class Staff(Person):
    DATA_FILE = "../data/staff.json"

    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee_id = employee_id

    @classmethod
    def staff_objects(cls):
        staff = []
        f = open('data/staff.json')
        data = json.load(f)

        for i in data:
            print(i)
            staff.append(i)
        return staff


class Student(Person):
    DATA_FILE = "./data/students.json"

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    @classmethod
    def student_objects(cls):
        student = []
        f = open('data/students.json')
        data = json.load(f)

        for i in data:
            print(i)
            student.append(i)
        return student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.staff_objects()
        self.students = Student.student_objects()

    def staff_names(self):
        staff_name = []
        data = self.staff
        for i in data:
            staff = [i['name'], i['employee_id']]
            staff_name.append(staff)
    
        return staff_name

    def student_names(self):
        student_name = []
        data = self.students
        for i in data:
            student = [i['name'], i['school_id']]
            student_name.append(student)
        return student_name

    def find_student_by_id(self, school_id):
        for student in self.students:
            if student['school_id'] == school_id:
                return student
        
        return None

    def find_staff_by_id(self, employee_id):
        pass


school = School('test')

print(f' answer = {school.find_staff_by_id(86545)}')
# print(school.students)