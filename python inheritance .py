#!/usr/bin/env python
# coding: utf-8

# In[25]:


# inheritance
# Determine if School_bus is also an instance of the Vehicle class
class vehicle:
    def __init__(self):
        print("This is vehicles")
    def color(self):
        print("The color is yellow")
    def model(self):
        print("This is latest model")
class school_bus(vehicle):
    def __init__(self):
        print("School bus is a vechicle")
    def color(self):
        super().color()
        print("The color is red")
school=school_bus()
school.color()
school.model()
# check school object instance of class vehicle
isinstance(school,vehicle)


# In[2]:


# Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.
# 2. setAge - It should assign age to student
# 3. setMarks - It should assign marks to the student.
class student:
    def __init__(self,n,r):
        self.name=n
        self.roll_num=r
    def display(self):
         print("Name is {} and the roll number is {}".format(self.name,self.roll_num))
#          print(f"Name is {self.name} and roll number is {self.roll_num}")
    def setage(self,age) :
        return "The age is {}".format(age)
    def setmark(self,mark):
        return "The mark is {}".format(mark)
        
students=student('anu',101)
students.display()
print(students.setage(15))
print(students.setmark(35))


# In[3]:


# multilevel inheritance
# create a class animal and create sub class dog, and based on dog create another subclass dogchild
class animal:
    print("This is animal")
class dog(animal):
    print("This is a dog")
class dog_child(dog):
    print("Is also dog")
dogc=dog_child()


# In[10]:


# multiple inheritance
# create classes calculation1,calculation2 with method summation ,multiplication and child class calculation 3 with method-
# division 
a=9
b=3
class calculation1:
    def sum(x,y):
        return (a+b)
class calculation2:
    def multipl(x,y):
        return (a*b)
class calculation3(calculation1,calculation2):
    def division(x,y):
        return (a/b)
calcu=calculation3()
print(calcu.sum(a+b))
print(calcu.multipl(a*b))
# print(calcu.division(a/b))


# In[42]:


# a=9
# b=3
class calculation1:
    def sum(self,x,y):
        print("Sum is ",x+y)
class calculation2:
    def multipl(self,x,y):
        print("Multiplication is :",x*y)
class calculation3(calculation1,calculation2):
    def division(self,x,y):
        print("Division is :",x/y)
calcu=calculation3()
calcu.sum(3,5)
calcu.multipl(3,5)
calcu.division(3,5)


# In[ ]:




