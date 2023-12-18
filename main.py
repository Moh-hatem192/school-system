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

    def __repr__(self):
        return f'Student(Name: {self.name} is in {self.grade} grade )'
    
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
                
class Teacher:
    All_Teachers = []
    def __init__(self, name, age, nationality, email, hours_worked, hourly_rate):
        self.name = name
        self.age = age
        self.__email = email
        self.nationality = nationality
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.nationality = nationality   
        Teacher.All_Teachers.append(self)

    def __str__(self):
        return f'{self.name} is {self.age} years old for conatact: {self.__email}'

    def __repr__(self):
        return f'Teacher(Name: {self.name} is  {self.age} years old )'
    
    @property
    def email(self):
        return self.__email
    
    @classmethod
    def create_instances(cls, file):
        with open(file) as f:
            teachers = csv.DictReader(f)
            for teacher in teachers:
                Student(
                    teacher.get('name'),
                    teacher.get('name'),
                    teacher.get('name'),
                    teacher.get('name'),
                    teacher.get('name'),
                    teacher.get('name')
                ) 
                        
osama = Teacher('ali',13,45,'asw','ahh',12)