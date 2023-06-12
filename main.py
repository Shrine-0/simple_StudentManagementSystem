from tqdm import tqdm
from time import sleep

# TODO  -- create a Student management system with a simple functionality for assigning grades  asses grades to max min and average and view them
# TODO -- Recursively call the student login function to store the student details in the list student list 
# ! -- student login  recursion required , student logout required a simple break might suffice

#  *model

class Grades:
    def __init__(self,subject,Grades=""):
        self.__Grades =Grades
        self.__subject = subject
    
    def GiveGrades(self):
        self.__Grades = Grades
        
    def setGrades(self,grades):
        self.__Grades = grades

            
class Student(Grades):
    def __init__(self,name="",age="",roll_no=0):
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


    
# *view
            
class StudentView:
    
    def __init__(self):
        pass
    
    def Grades(self):
       print("the grades") 
       
    def Grades_maximum(self):
        print("maximum grades")
        
    def Grades_average(self):
        print("Average grades")
        
# *controller
class StudentLog:
    def __init__(self):
        # self.name 
        # self.age
        pass
   
        
    
    def Login(self,check):
        if(check is not True):
            for i in tqdm(range(100),desc="loading",leave=False):
                sleep(0.0035)
            print("Exited")
            exit()
        # while True:
        student_model_objects_list= [Student() for i in range(10)]
        try:
           
            for i in range(len(student_model_objects_list)):
                self.name = input(f"Student Name -- at index {i} : ")
                student_model_objects_list[i].setname(self.name)
                self.age  = input(f"Student Age  -- at index {i} :")
                student_model_objects_list[i].setage(self.age)
            
                # return student_model_objects_list[i] ## student object return 
            
        except ValueError:
            print("name not valid ")
            
        finally:
            
            for i in range(10):
                print(f"Name : {student_model_objects_list[i].getname} \nAge : {student_model_objects_list[i].getage}")
            return student_model_objects_list
        
            
class GradesAsseser:
    def __init__(self):
        pass    
    def GradesMaximum(self):
        pass
        
        
        
def main():
    log = StudentLog()
    checker = input("do you want to login ( Y / n ) : ")
    if tocheck:= checker == "Y" or checker == 'y':
        student_list = log.Login(tocheck)
        print(student_list)
    else :
        log.Login(tocheck)
        # GA.Login(False)    


if __name__ == "__main__":
    main()
        

        
        

    