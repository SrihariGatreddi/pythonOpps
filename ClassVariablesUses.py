'''class ABC():
    class_var=0
    def __init__(self,var) -> None:
        ABC.class_var+=1
        self.var=var
        print('class variable value',ABC.class_var)
        print('obj var value:',var)
obj1=ABC(10)
obj2=ABC(20)'''
'''class Number():
    even=0
    def check(self,num):
        if num%2==0:
            self.even+=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print("even")
            print(self.even)
            print(Number.even)
        else:
            print("odd")
n1=Number()
n1.even_odd(20)
n2=Number()
n2.even_odd(21)
print(n1.even)#to demonstarte that the class variable here is to be constant value to every object and changes made is effexted to that particular object 
print(n2.even)
print(Number.even)'''
#to demonstrate mutable objects are changable over objects calling
'''class Number():
    evens=[]
    odds=[]
    def __init__(self,num) -> None:
        if num%2==0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)
N1=Number(20)
N2=Number(34)
N3=Number(21)
N4=Number(25)
N5=Number(2)
N6=Number(22)
N7=Number(41)
print("evens:",Number.evens)
print("odds:",N1.odds)#prints same as number.odds as the changes are made in every objects simultaneously
            '''
class Number():
    evens=[]
    odds=[]
    def __init__(self,num) -> None:
        if num%2==0:
            self.evens.append(num)#instaed number.odss... self.odss works same by changing class attributes to change in all objects
        else:
            self.odds.append(num)
N1=Number(20)
N2=Number(34)
N3=Number(21)
N4=Number(25)
N5=Number(2)
N6=Number(22)
N7=Number(41)
print("evens:",Number.evens)
print("odds:",Number.odds)            