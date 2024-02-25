class Student(object):#parent class of all the serived class is "object" that is defined by default in built-in
    def __init__(self,id):
        self.college='Raghu Engineering College'
        self.branch='CSM-A'
        self.id=id
class basic_det(Student):
    def __init__(self,name,rollno,id):
        super().__init__(id)#super class for basic_det is Student
        self.name=name
        self.rollno=rollno
        #print(f'NAME: {self.name} \n ROLLNO:{self.rollno} \n COLLEGE:{self.college} \n BRANCH:{self.branch} \n ID={self.id} ')
class StudentSrihari(basic_det):
          def __init__(self, name, rollno, id,bloodG):
               super().__init__(name, rollno, id)#super class for student srihari is basic det
               self.bloodGroup=bloodG
               print(f'NAME: {self.name} \n ROLLNO:{self.rollno} \n COLLEGE:{self.college} \n BRANCH:{self.branch} \n ID={self.id} \n Blood Group:{self.bloodGroup}')
stu1=StudentSrihari('srihari',229814241,4241,'A+')
print(stu1.id)   
print(stu1.id)
print(StudentSrihari.mro())#returns list
print(StudentSrihari.__mro__)#returns tupple