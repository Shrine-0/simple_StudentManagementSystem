
#TODO  -- create a Student management system with a simple functionality for assigning grades  asses grades to max min and average and view them

class Student:
    def __init__(self,name,age,roll_no):
        self.__name = name
        self.__age = age
        self.__roll_no = roll_no
        
    # @name.setter
    def setname(self,name):
        if  not isinstance(name,str):
            raise ValueError("Must be a string")
        self.__name = name
    @property
    def getname(self):
        return self.__name
        
    # @age.setter
    def setage(self,age):
        self.__age = age
        
    @property
    def getage(self):
        return self.__age
    
    def setroll_no (self,roll_no):
        self.__roll_no = roll_no
    
    @property
    def getrollno(self):
        return self.__roll_no
    
    
class StudentView:
    def view():
        pass