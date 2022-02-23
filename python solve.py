#!/usr/bin/env python
# coding: utf-8

# In[1]:


# print first and last name in reverce order with a space between them
str="manjima arun"[::-1]
print("The reverce is :",str)


# In[2]:


# Calculate the sum of three given numbers, if the values are equal then return thrice of their sum
def sum_of(x,y,z):
    if x==y==z:
        sum=(x+y+z)*3
        return sum
    else:
        sum=x+y+z
        return sum
print("Sum of three given numbers :",sum_of(1, 2, 3))
print("Thrice of their sum :",sum_of(3, 3, 3))


# In[3]:


# generat a list and tuple with comma superated numbers
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# In[4]:


# Get a single string from two given strings, separated by a space and swap the first two characters of each string
str1="Anu"
str2="Raju"
temp=str1[1]
str1=str1.replace(str1[1],str2[1]) 
str2=str2.replace(str2[1],temp)
print("Change in first string :",str1)
print("Change in second string :",str2)


# In[5]:


# Write a Python program to print out a set containing all the colors from color1 which are not present in color2.
# difference
color1=set(["blue","black","green"])
color2=set(["blue","yellow"])
x=color1-color2
print("Color1 which are not present in color2 :",x)


# In[6]:


# convert a string to list
str1="hii hallo world"
list1=str1.split()
print(list1)


# In[7]:


# Write a Python function to multiply all the numbers in a list.
list1=[1,2,3,10]
def multiply(num):
    x=1
    for i in num:
        x=x*i
    return x
print(multiply(list1))


# In[8]:


# Find common items from two lists
list1=["car","bus","train"]
list2=["car","cycle","auto","train"]
val=set(list1) & set(list2)
print("common items in two lists :",val)


# In[9]:


# Find common items from two lists
list1=["car","bus","train"]
list2=["car","cycle","train"]
for i in list1:
    for j in list2:
        if i==j:
            print(i)


# In[10]:


# Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. Create a 
# function to display the entire attribute and their values in Student class.
class student:
    student_id='100'
    student_name='Ankitha'
    def display():
        print("Student id is :{}".format(student.student_id))
        print("Student name is :{}".format(student.student_name))
print("Original attributes and their values of the Student class:")
student.display()        


# In[11]:


# Write a Python program to access a function inside a function.
def double(num):
    def add(num):
        return num+num
    m=add(num)
    print("The number is :",num)
    print("The double is :",m)
double(3)


# In[12]:


# create class animal with method speak and child class Dog inherits the base class Animal 
class animal:
    def __init__(self):
        print("animal is ready")
    def this(self):
        print("animal")
    def runing(self):
        print("runing faster")
class dog(animal):
    def __init__(self):
        super().__init__()
        print("dog is ready")
    def this(self):
        print("dog") 
    def run(self):
        print("Run fast")
jimmy=dog()  
jimmy.this()
jimmy.runing() 
jimmy.run()


# In[16]:


# python program to create a class which performs basic calculation operations
class calculater:
    def add(x,y):
        return(a+b)
    def substract(x,y):
        return(a-b)
    def mult(x,y):
        return(a*b)
    def division(x,y):
        return(a/b)
    a=int(input("Enter first number :"))
    b=int(input("ENter second number :"))
calculation=calculater()
print("The addition of two numbers :",calculation.add(a+b))
print("The substraction of two numbers :",calculation.substract(a-b))
print("The multiplication of two numbers :",calculation.mult(a*b))
print("The division of two numbers :",calculation.division(a/b))

