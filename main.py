import csv
teachers_users = {
    'Ali Ahmad':{
        'user': 'ali ahmad',
        'password': '1234'
    },
    'teacher':{
        'user': '',
        'password': ''
    },
    'teacher':{
        'user': '',
        'password': ''
    },
    'teacher':{
        'user': '',
        'password': ''
    },
    'teacher':{
        'user': '',
        'password': ''
    }
}

students_users = {
    'Ali Ahmad':{
        'user': 'ali ahmad',
        'password': '1234'
    },
    'teacher':{
        'user': '',
        'password': ''
    },
    'teacher':{
        'user': '',
        'password': ''
    },
    'teacher':{
        'user': '',
        'password': ''
    },
    'teacher':{
        'user': '',
        'password': ''
    }
}

class Student:
    All_Students = []
    Students_Names = []
    def __init__(self, name, age, DOB, grade, nationality, address):
        self.name = name
        self.age = age
        self.dob = DOB
        self.grade = grade
        self.nationality = nationality
        self.address = address        
        Student.All_Students.append(self)
        Student.Students_Names.append(self.name.title())
    
    def __str__(self):
        return f'{self.name} is {self.age} years old and in {self.grade} grade'

    def __repr__(self):
        return f'Student(Name: {self.name} is in {self.grade} grade )'
    
    @classmethod
    def take_user_details(cls):
        name = input('Please enter your name: ').title()
        if name not in Student.Students_Names:
            print("sorry you are don't have access to the system")
        else:
            password = input('Please enter your account password: ')
            if password != students_users.get(name).get('password'):
                print("Incorrect Password")  
            else:
                print('Login succeed')

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
    Teachers_Names = []
    def __init__(self, name, age, nationality, email, hours_worked, hourly_rate):
        self.name = name
        self.age = age
        self.__email = email
        self.nationality = nationality
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.nationality = nationality   
        Teacher.All_Teachers.append(self)
        Teacher.Teachers_Names.append(self.name.title())
    
    def __str__(self):
        return f'{self.name} is {self.age} years old for conatact: {self.__email}'

    def __repr__(self):
        return f'Teacher(Name: {self.name} is  {self.age} years old )'
    
    @property
    def email(self):
        return self.__email
    
    @classmethod
    def take_user_details(cls):
        name = input('Please enter your name: ').title()
        if name not in Teacher.Teachers_Names:
            print("sorry you are don't have access to the system")
        else:
            password = input('Please enter your account password: ')
            if password != teachers_users.get(name).get('password'):
                print("Incorrect Password")  
            else:
                print('Login succeed')
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

    def calculate_gross_salary(self):
        return self.hourly_rate * self.hours_worked

    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        net_salary = Finance.calculate_net_salary(gross_salary)
        return net_salary

class Finance:
    INSURANCE = 100
    HIGH_RATE = 0.2
    LOW_RATE = 0.12
    RETIRMENT = 50

    @staticmethod 
    def calculate_net_salary(salary):
        if salary >= 1200:
            deductions = Finance.INSURANCE + (Finance.HIGH_RATE*salary) + Finance.RETIRMENT
            net_salary = salary = deductions
        else:
            deductions = Finance.INSURANCE + (Finance.LOW_RATE*salary) + Finance.RETIRMENT
            net_salary = salary = deductions    
        return net_salary    

osama = Student('ali ahmad', 2, 3, 4, 5, 6,)  

def main():
    while True:
        print('Welcome to Codezilla school')
        user = input('Are you a student or a teacher: ').lower()
        if user == 'teacher' or user == 't':
            Teacher.take_user_details()
            break
        else:
            Student.take_user_details()
            break

if __name__ == '__main__':
    main()