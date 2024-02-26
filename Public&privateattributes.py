class ABC():
    def __init__(self,var1,var2) -> None:
        self.var1=var1
        self.__var2=var2
    def display(self):
        print("from class accesing var1..var1=",self.var1)
        print("from class accesing private var2..var2=",self.__var2)
obj=ABC(10,20)
obj.display()
print("from main module accesing var1..var1=",obj.var1)
print("from main module accesing private  var2..var2=",obj._ABC__var2)      
print("from main module accesing private  var2..var2=",obj.__var2)#if want to access private attibute of class from main module syn:obj._ABC__var2

        
        
        
           