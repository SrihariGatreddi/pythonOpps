class Student():
    def __init__(self,id):
        self.college='Raghu Engineering College'
        self.branch='CSM-A'
        self.id=id
class basic_det(Student):
    def __init__(self,name,rollno,id):
        super().__init__(id)
        self.name=name
        self.rollno=rollno
        print(f'NAME: {self.name} \n ROLLNO:{self.rollno} \n COLLEGE:{self.college} \n BRANCH:{self.branch} \n ID={self.id} ')
stu1=basic_det('srihari',22984241,2298)
print(stu1.id)   