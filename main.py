from tqdm import tqdm
from time import sleep

# TODO  -- create a Student management system with a simple functionality for assigning grades  asses grades to max min and average and view them
# ! --  add course logic and find the answer for bound object to string 
# ! -- assign roll no on index numbers 

#  *model
class Course:
    
    def __init__(self,coursename):
        self.__courseName = coursename
        
    def __str__ (self):
        return self.__courseName
    
    @property
    def coursename(self,coursename):   
        self.__courseName = coursename
        
    @coursename.setter
    def getcourse(self):
        return self.__courseName


class Grades:
    def __init__(self,subject,Grades):
        self.__Grades =Grades
    
    def __str__(self):
        return f"{self.__Grades}"
    
    @property
    def Grades(self):
        return self.__Grades 
    
    @Grades.setter   
    def setGrades(self,grades):
        self.__Grades = grades

class Student(Grades,Course):
    def __init__(self,name="",age=""):
        self.__name = name
        self.__age = age
        self.__roll_no = 0

    def __str__(self):
        return f"{self.__name}({self.__age})--{self.__roll_no}"
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def setname(self,name):
        if  not isinstance(name,str):
            raise ValueError("Must be a string")
        self.__name = name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def setage(self,age):
        self.__age = age
        
    @property
    def rollno(self):
        return self.__roll_no

    @rollno.setter
    def setroll_no (self,roll_no):
        self.__roll_no = roll_no
    

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
        student_model_objects_list= [Student() for i in range(2)]

        try:
           
            for i in range(len(student_model_objects_list)):
                
                self.name = input(f"Student Name -- at index {i} : ")
                student_model_objects_list[i].setname(self.name)
                
                self.age  = input(f"Student Age  -- at index {i} :")
                student_model_objects_list[i].setage(self.age)
                
                self.grade = input(f"student at index -- {i} grade : ")
                student_model_objects_list[i].Grades(self.grade)
                
            return student_model_objects_list

        except ValueError:
            print("name not valid ")
            
        finally:
            # for i in range(2):
            #     print(f"Name : {student_model_objects_list[i].getname} \nAge : {student_model_objects_list[i].getage}\nGrades : {student_model_objects_list[i].GiveGrades}")
            pass
            
        
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
        print(student_list[1])
    else :
        log.Login(tocheck)
        # GA.Login(False)    


if __name__ == "__main__":
    main()
        

        
        

    