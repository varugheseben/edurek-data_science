# class Student:
#     pass


# s1 = Student()
# print(s1)

# class Student:

#     ## methods 

# x = "akshat"
# print(x)  #akshat
# print(type(x))

# # change to upper letter
# print(x.upper()) #Method : function which is present inside the class 


# y = str("Akshat")   #akshat  #str is class
# print(y)
# print(y.upper())

# class School:
#     def student(self):  #self = d1  # self is the object but rather then hardcoding the object name if you put self it does not matter what object name your create
#         print("hello")
#     def classroom(self):
#         print("welcome to class")

# d1 = School()  #creating the object d1 where i will call class School
# d1.student()  # i am calling method student
# # class School:
#     # def student(d1)
# d1.classroom()

# myschool = School()
# myschool.student()
# akshat = School()    # we have object akshat
# akshat.student()

# class School:
#     def student(self):  #method named student in class School
#         print(f"Name is {self.name}")
#     def classroom(self):
#         print(f"The student class is {self.school_name}")   #a1.school_name

# #  we need to create object name a1
# a1 = School()  # we are creating where we will call class
# a1.name = "Akshat"  #We are saying that object.variable = "Akshat"
# a1.student()
# a1.school_name = "gurukul"
# a1.classroom()


# ## another way 
# class School:
#     def student(self,name,sex):  #method named student in class School ## student(a1,"akshat")
#         # internally : name = "akshat" and sex =  Male
#         print(f"Name is {name} and is {sex}")
#    #o/p: Name is AKshat and is Male
#     def classroom(self,school_name):
#         #internally : school_name = "Mygurukul"
#         print(f"The student class is {school_name}")   #a1.school_name

# #  we need to create object name a1
# a1 = School()  # we are creating where we will call class
# a1.student("AKshat","Male")  # we are calling the method student with object a1 and variable name=akshat
# a1.classroom("Mygurukul")


#Constructor


# class College: 
#     def student(self):
#         print("Hello student")

# d1 = College()
# ## till here it will not print anything until we call method
# ## Lets say we want that as soon an object is created the some value should 
# # execute and thats constructor

# using constructor
class College: 
    def __init__(self):  #method __init__ which has property to execute as soon as the class is created : constructor
        print("this will execute as soon as you create object...you dont have to call method")
    def student(self):
        print("Hello student")

d1 = College()
##o/p: this will execute as soon as you create object...you dont have to call method
## since we are using constructor we get output as constructor executes after object is created 

d1.student()
## Hello student will  also be printed