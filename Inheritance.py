class human():
    name='srihari'
    rollno='22981a4241'
    def __init__(self,heart,phnno) -> None:
        self.heart=heart
        self.studentid=9872
        self.phnno=phnno
    def eat(self):
        print('i can eat')
    def work(self):
        self.id=9889
        print('i can work')
class male(human):
    print(human.name)
    def __init__(self,name,heart,phnno) -> None:
        super().__init__(heart,phnno)#to access the parent class attributes in the base class
        super().work()
        self.name1=name
        print(self.name1)
        print(self.studentid)
        print(self.studentid)
    def greetings(self):
        print('hello everyone ..how are you!!')
    def work(self):
        super().work()#to inherit work from superclass
        print("i can code")#over writing the work method from parent class
    def display(self):
        print(f'im {self.name}  and rollno {self.rollno}')
male_1=male('srihari',1,9182860457)
male_1.eat()
male_1.greetings()
male_1.work()
print(male_1.heart)
male_1.display() 
print(male_1.id)

