from tqdm import tqdm
from time import sleep

# TODO  -- create a Student management system with a simple functionality for assigning grades  asses grades to max min and average and view them
# ! --  add course logic and find the answer for bound object to string 
# ! -- assign roll no on index numbers 

#  *model
class Course:
    
    # ! -- class attributes or static variabel declaration and initialization below
    total_course_no = 0
    
    def __init__(self,coursename):
        self.__coursename = coursename
        
    def __str__ (self):
        return self.__coursename
    
    @classmethod
    def total_no(cls):
        print(f"Total no of courses currently added : {Course.total_course_no}")
    
    @property
    def coursename(self):
        return self.__courseName
    
    @coursename.setter
    def coursename(self,coursename):   
        if not isinstance(coursename,str):
            raise ValueError("name must be a string")
        self.__coursename = coursename
        Course.total_course_no +=1

class Grades:
    def __init__(self,subject,Grades):
        self.__grades =Grades
    
    def __str__(self):
        return f"{self.__Grades}"
    
    @property
    def grades(self):
        return self.__Grades 
    
    @grades.setter   
    def grades(self,grades):
        if not isinstance(grades,str):
           raise ValueError("must be charecter from A to F") 
        self.__grades = grades

class Student(Grades,Course):
    
    number_of_students = 0
    
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
    def name(self,name):
        if  not isinstance(name,str):
            raise ValueError("Must be a string")
        self.__name = name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age < 0 :
            raise ValueError("Age must be appropriate")
        self.__age = age
        
    @property
    def rollno(self):
        return self.__roll_no

    @rollno.setter
    def rollno (self,roll_no):
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
                student_model_objects_list[i].name = self.name
                
                self.age  = input(f"Student Age  -- at index {i} :")
                student_model_objects_list[i].age = int(self.age)
                
                self.grades = input(f"student at index -- {i} grade : ")
                student_model_objects_list[i].grades = self.grades
                
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
    Course.total_no()


if __name__ == "__main__":
    main()
        

        
        

    