from tqdm import tqdm
from time import sleep,time

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
        return Course.total_course_no
    
    @classmethod 
    def increment(cls):
        Course.total_course_no +=1
    
    @property
    def coursename(self):
        return self.__courseName
    
    @coursename.setter
    def coursename(self,coursename):   
        if not isinstance(coursename,str):
            raise ValueError("name must be a string")
        self.__coursename = coursename
        Course.increment()

class Grades:
    def __init__(self,grades):
        self.__grades =grades
    
    def __str__(self):
        return f"{self.__grades}"
    
    @property
    def grades(self):
        return self.__grades 
    
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
        return f"Name : {self.__name}\nAge : {self.__age}\nroll_no : {self.__roll_no}\nGrades : {self.grades}"
    
    @classmethod
    def total_students(cls):
        print(f"total no of students : {Student.number_of_students}")
        return Student.number_of_students
    
    @classmethod
    def increment(cls):
        Student.number_of_students+=1
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if  not isinstance(name,str):
            raise ValueError("Must be a string")
        self.__name = name
        Student.increment()
        
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
    def rollno (self):
        self.__roll_no = Student.number_of_students
        
    

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
                
                # self.name = input(f"Student Name -- at index {i} : ")
                self.name = input("Student Name : ")

                student_model_objects_list[i].name = self.name
                
                # self.age  = input(f"Student Age  -- at index {i} :")
                self.age  = input("Student Age : ")
                student_model_objects_list[i].age = int(self.age)
                
                # self.grades = input(f"student at index -- {i} grade : ")
                self.grades = input("students grade in course {course.} : ")
                student_model_objects_list[i].grades = self.grades
                
            return student_model_objects_list

        except ValueError:
            print("name not valid ")
            
        finally:
            # for i in range(2):
            #     print(f"Name : {student_model_objects_list[i].name} \nAge : {student_model_objects_list[i].age}\nGrades : {student_model_objects_list[i].grades}")
            pass
            
        
class GradesAsseser:
    def __init__(self):
        pass    
    def GradesMaximum(self):
        pass
        
        
def main():
    t1 = time()
    log = StudentLog()
    checker = input("do you want to login ( Y / n ) : ")
    if tocheck := checker == "Y" or checker == 'y':
        student_list=log.Login(tocheck)
    else :
        log.Login(tocheck)
        # GA.Login(False) 
    Course.total_no()

    for i in range(2):
        print(student_list[i])
        
    # print([student_list[i].__str__ for i in range(len(student_list))])
    
    t2 = time()
    print(f"the program took a complete of {t2-t1} secs")
   



if __name__ == "__main__":
    main()
        

        
        

    