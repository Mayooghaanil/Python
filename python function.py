#!/usr/bin/env python
# coding: utf-8

# In[3]:


# function
def greet(name):
    """This function greets to the person passed in a parameter"""
    print("hello,"+name+".Good morning!")


# In[4]:


# function call
hii("a")
# function defanition
def hii(a):
    print("hiii"+a)


# In[5]:


# function call
greet('xyz')
# function definition
def greet(sam):
    """This function greets to the person passed in a parameter"""
    print("hello,"+sam+".Good morning!")


# In[6]:


# to call a function
# function definition
def greet(name):
    """This function greets to the person passed in a parameter"""
    print("hello,"+name+".Good morning!")
# function call
greet('anu')


# In[7]:


# availabe in document string
def greet(name):
    """This function greets to the person passed in a parameter"""
    print("hello,"+name+".Good morning!")
greet('anu')
print(greet.__doc__)


# In[8]:


print(greet("may"))


# In[9]:


def absalute_value(num):
    """function return absalute value of the number"""
    if num>0:
        return num
    else:
        return -num
print(absalute_value(2))
print(absalute_value(-4))


# In[10]:


def my_func():
    num=10
    print("Value in side the function",num)
num=20
my_func()
print("Value outside the function",num)


# In[11]:


def add_number(x,y):
    add=x+y
    return add
num1=5
num2=6
print("The sum is",add_number(num1,num2))


# In[12]:


def may(name,msg):
    """name and message"""
    print("hello",name+","+msg)
may("mayoogha","welcome to python")


# In[17]:


# 2 keyword arguments
# in keyword argument
def greet(name,msg="Good morning"):
    """name and message pass in different ways"""
    print("hello",name+msg)
greet("manu ")
greet("manu ","welcome")


# In[24]:


# 2 keyword arguments
# in keyword argument
def greet(name,msg):
    """name and message pass in different ways"""
    print("hello",name+msg)
greet(name="aan ",msg="how do you do")


# In[26]:


# 2 keyword arguments
# one keyword argument and one position argument
def greet(name,msg):
    """name and message pass in different ways"""
    print("hello",name+msg)
greet("ammu ",msg="how do you do")


# In[29]:


# 2 keyword arguments
#  first keyword argument and position argument is error
   
def greet(name,msg):
   """name and message pass in different ways"""
   print("hello",name+msg)
greet(msg="how do you do","ammu ")


# In[53]:


# recursion
def factorial(x):
    """To find factorial of number"""
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=3
print("the factorial of num is",factorial(num))


# In[36]:


# python anonymous/lambda function
double=lambda x:x*2
print(double(5))


# In[39]:


# is near the same as
def double(x):
    return x*2
double(4)


# In[5]:


# filter out only the even items from the list
my_list=[1,2,3,4,5,6,7,8]
new_list=list(filter(lambda x:(x%2==0),my_list))
print(new_list)


# In[1]:


# program to double each item in a list using map()
my_list=[1,2,3,4,12,6]
new_list=list(map(lambda x:x*2,my_list))
print(new_list)


# In[3]:


# global and local variable 
x="global"
def foo():
    print("x inside is :",x)
foo()
print("x outside is :",x)        


# In[7]:


# error her modifyning global variable in function
x="global"
def foo():
    x=x*2
    print(x)
foo()


# In[9]:


# error
c=1
def add():
    c=c+2
    print(c)
add()


# In[10]:


# the solution for this is to use the global keyword
c=0
def val():
    global c
    c=c+2
    print("inside function :",c)
val() 
print("in main :",c)


# In[12]:


# error accessing local variable outside the scope
def foo():
    y="local"
foo()
print(y)


# In[13]:


# creat a local variable
def value():
    y="local"
    print(y)
value()


# In[20]:


# using global and local variable in same code
x="global"
def foo():
    global x
    y="local"
    x=x*2
    print(x)
    print(y)
foo()


# In[25]:


# global variable and local variable in same name
x=5
def foo():
    x=10
    print("local x :",x)
foo()
print("global x :",x)


# In[1]:


# function call two times
def foo():
    print(1)
    print(2)

foo()
foo()


# In[3]:


def foo(x, y):
    if x >= y:
        return x
    else:
        return y

x = foo(4, 7)
print(x)


# In[6]:


def print_numbers():
    print(1)
    print(2)
    return
print(4)
print(6)


# In[7]:


def sum(x):
    res = 0
    for i in range(x):
        res+=i
    return res
    
print(sum(4))


# In[17]:


def print_nums(x):
    for i in range(x):
        print(i)
        return
print_nums(10)


# In[ ]:




