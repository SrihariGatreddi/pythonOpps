class Student():
    def __init__(self,id):
        self.college='Raghu Engineering College'
        self.branch='CSM-A'
        self.id=id
    def grade(self):
        print('Student Grade is A+')
class College_det():
    college_aff='JNTUGV'
    Naac_Grade='A+'
    def __init__(self,strength):
        self.student_strength=strength            
    def grade(self):
        print('college grade is A+')
class basic_det(Student,College_det):
    def __init__(self,name,rollno,id,strength):#argumenets that are given to derived __init__ must be equal to total parameters passed to both base classes+self attributes od derived class if any
        Student.__init__(self,id)
        College_det.__init__(self,strength)#to access attributes of base classes
        self.name=name
        self.rollno=rollno
        print(f' NAME: {self.name} \n ROLLNO:{self.rollno} \n COLLEGE:{self.college} \n BRANCH:{self.branch} \n ID={self.id} \n College_Affiliated={self.college_aff} \n Nacc_Grade={self.Naac_Grade} ')
    def grade(self):
        print('my job grade is A+')#grade in this devived class is first accessed when called,if not present then seach in base classes
    def display(self):
        print(f"hai im {self.name} and i inherited my id i.e {self.id} and my clg strength -{self.student_strength}")
stu1=basic_det('srihari',22984241,2298,7000)
print(stu1.id) 
print(stu1.college_aff)
print(stu1.grade())#since there are 2 methods with same name 'grade' 1st defined class is 'student' grade fun from student class is accesed 
#to accesses grade fun from college_def directly
print(College_det.grade(stu1))
print(basic_det.mro())#prints heirarchy of the searching the method i.e from derived to base classes
print(stu1.student_strength)
print(stu1.display())