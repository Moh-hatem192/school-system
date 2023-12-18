import csv
class Student:
    All_Students = []
    def __init__(self, name, age, DOB, grade, nationality, address):
        self.name = name
        self.age = age
        self.dob = DOB
        self.grade = grade
        self.nationality = nationality
        self.address = address        
        Student.All_Students.append(self)

    def __str__(self):
        return f'{self.name} is {self.age} years old and in {self.grade} grade'

    @classmethod
    def create_instances(cls, file):
        with open(file) as f:
            students = csv.DictReader(f)
            for student in students:
                Student(
                    student.get('name'),
                    student.get('name'),
                    student.get('name'),
                    student.get('name'),
                    student.get('name'),
                    student.get('name'),
                ) 