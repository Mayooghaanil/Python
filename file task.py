#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a Python program to read an entire text file.
f=open("kjxcckjzxck.txt",'r',encoding='utf-8')
print(f)


# In[2]:


# Python Program to Read the Contents of a File
f=open("kjxcckjzxck.txt",'r',encoding='utf-8')
f.read()


# In[3]:


# Python Program to Count the Number of Lines in a Text File
f=open("kjxcckjzxck.txt",'r',encoding='utf-8')
f.readlines()


# In[4]:


# Python Program to Read a Text File and Print all the Numbers Present in the Text File
with open("kjxcckjzxck.txt",'r',encoding='utf-8') as file:
    for line in file:
        for letter in line:
                if(letter.isdigit()):
                    print(letter)


# In[5]:


# Python Program to Copy a File
import shutil
shutil.copyfile('kjxcckjzxck.txt','kjxcc.txt')


# In[6]:


# Count number of lines in a text file in Python
with open("kjxcckjzxck.txt",'r',encoding='utf-8') as file:
    x=len(file.readlines())
    print("Total line is :",x)


# In[7]:


# Write a Python program to append text to a file and display the text.
with open("kjxcckjzxckjj.txt",'w',encoding='utf-8') as f:
    f.write("This is appanding line")
f=open("kjxcckjzxckjj.txt",'r',encoding='utf-8')
print(f.read())


# In[8]:


# Python program to demonstrate KeyError
dict={1:"one",2:"two",3:"three"}
print("The dictnory is :",dict)
print(dict[4])


# In[ ]:


# Python program to demonstrate IndexError
fruits = ['Apple', 'Banana', 'Guava']  
print("Type is", type(fruits))  
fruits[5] = 'Mango'


# In[ ]:


# Python Program to Handle Divide by Zero Exception
n=int(input("Enter the value :"))
try:
    val=1/n
    print(val)
except ZeroDivisionError:
    print("Division by Zero!")


# In[ ]:


# Python program to demonstrate AttributeError
X = 10
X.append(6)


# In[ ]:


# Python program to demonstrate NameError
name = input()
print(value)


# In[2]:


# program to show that we can create instance variables inside methods
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student('Ammu', 18)
s2 = Student('Appu', 70)

print(s1.name)
print(s2.name)


# In[1]:


# Create a function that will throw an exception if interest rate is greater than 100.
def value(a):
    try:
        if a>100:
            raise ValueError("This is greater than 100")
        else:
            print("correct input")
    except ValueError as ve:
        print(ve)  
value(488)


# In[ ]:




