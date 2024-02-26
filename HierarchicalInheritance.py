class Student(object):
    section='csm-a'
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
class NCC_Cadet(Student):
    certificate='A'
    def __init__(self, name, age,Battalion) -> None:
        Student.__init__(self,name, age)
        self.Battalion=Battalion
class NSS_Cadet(Student):
    certificate='A+'
    def __init__(self,name,age,tshirtcolr) -> None:
        Student.__init__(self,name,age)
        self.tshirt=tshirtcolr
class Srihari(NCC_Cadet,NSS_Cadet):
    def __init__(self,name, age, Battalion,tshirt):
        NCC_Cadet.__init__(self,name, age, Battalion)   
        NSS_Cadet.__init__(self,name,age,tshirt)
    def display(self):
        print(f"NAME:{self.name}\nAGE:{self.age}\nNSS DETAILS OF {self.name}\n 1.CERTIFICATE:{NSS_Cadet.certificate}\n 2.T-SHIRT COLOR:{self.tshirt}\nNCC DETAILS OF {self.name}:\n 1.CERTIFICATE:{self.certificate}\n 2.BATTALION:{self.Battalion}")   
stu_1=Srihari('srihari',19,'VZM','GREEN')  
stu_1.display()
NSS1=NSS_Cadet('srihari',19,'green')
NCC1=NCC_Cadet('SRIHARI',19,'VZM')
print(NSS1.name)
print(NCC1.name)
print(stu_1.name)# in herited from grandparent