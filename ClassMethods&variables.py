class PersonalInfo():
    a=10
    followers=0
    def __init__(self,name,rollno,bloodG):
        self.stu_name=name
        self.stu_rollno=rollno
        self.stu_bloodG=bloodG
    def display(self,college_name):
        print(f"hai this is {self.stu_name} and my rollno is {self.stu_rollno} im from {college_name}")#no need to use self. as college name is not a class memeber
    def followers_update(self,followername):
        self.followers+=1#if personal_info.followers used it comes under single class varialbe used among various objects
        list=[]
        list.append(followername)
        for user in list:
            print(user)
student1=PersonalInfo('srihari',229814241,'a+')
student2=PersonalInfo('Navven',229814242,'b+')
print(student1.stu_name)
print(student1.a)   
student1.display('Raghu Engineering College')# need pass a argument bacause college name is not initialized as a class member
student2.display('raghu engineering college') 
student1.followers_update('abhishek_vasupalli099') 
student1.followers_update('manikanta') 
student1.followers_update('satwik') 
student1.followers_update('rohan') 
student1.followers_update('indu')
student2.followers_update('hari') 
print(student1.followers)
print(student2.followers)
