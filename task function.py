#!/usr/bin/env python
# coding: utf-8

# In[1]:


# print employee name and salary,default salary is 9000
def showemployee(name,salary=9000):
    """employee name and salary"""
    print("The name is:",name)
    print("The salary is:",salary)
showemployee("Amar","1000")


# In[2]:


# Add and substract two number in one function
def calculation(x,y):
    return(x+y,x-y)
num1=10
num2=5
print("The sum and substraction are :",calculation(num1,num2))


# In[3]:


# find largest number in list
list1=[5,15,8]
a=max(list1)
print("The large number is :",a)


# In[4]:


# Pass two argument name and age and print value
def person(name,age):
    """Enter name and age"""
    print("The name is:",name)
    print("The age is:",age)
person("Arjun","25")


# In[5]:


# print square of number in given list
my_list=[1,2,3,4,5,6]
new_list=list(map(lambda x:x*x,my_list))
print("Old list is :",my_list)
print("Square of list is :",new_list)


# In[6]:


# program to find numbers divisible by another number
list_1=[10,11,12,13,14,15]
list_2=list(filter(lambda x:x%5==0,list_1))
print("The list is :",list_1)
print("Number that are divisible by 5 are :",list_2)


# In[7]:


# to print fibinacci series
n=int(input("Enter the limit :"))
def fibin(num):
    """To find the fibinacci series"""
    if num==1:
        return 1
    elif num==0:
        return 0
    else:
        return fibin(num-1)+fibin(num-2)
print("fibinoci series are")  
for i in range(0,n):
    print(fibin(i))


# In[8]:


# factorial of number
num=int(input("Enter the number :"))
def factorial(x):
    """To find factorial of number"""
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print("the factorial of num is :",factorial(num))


# In[9]:


# find sum of n natural numbers
def sum_of(n):
    """find sum"""
    if n <= 1:
        return n
    else:
        return n + sum_of(n-1)
print("The sum is")
sum_of(3)    


# In[17]:


# check amstromg number
def chek(numb):
    global rslt_sum
    if (numb != 0):
        k = numb % 10
        rslt_sum += pow(k, 3)
        chek(numb//10)
    return rslt_sum
numb =int(input("Enter the number :"))
rslt_sum = 0
if (chek(numb) == numb):
    print("The Number is an Armstrong Number.")
else:
    print("The Number is Not an Armstrong Number.")


# In[29]:


# check palindrome
string="malayalam"
def palindrome():
    if string == string[::-1]:
        print("is palindrom")
    else:
        print("is not palindrom")
palindrome()

