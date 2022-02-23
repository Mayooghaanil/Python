#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=2
if a==0:
    print("The value is zero")
else:
    print("The cube is :",a**3)


# In[2]:


a=2
b=3
c=5
if a>b and a>c:
    print("a is large")
elif b>c:
    print("b is large")
else:
    print("c is large")


# In[3]:


a=34
if a%2==0:
    print("even number")
else:
    print("odd number")


# In[4]:


a=-23
if a>0:
    print("a is positive number")
else:
    print("a is negative number")


# In[5]:


a=0
print("numbers are")
for i in range(1,10,2):
    print(i)
    a=a+i
print("sum of numbers :",a)


# In[6]:


subject=[90,72,65,85,88]
x=0
for i in subject:
    x=x+i
print("total mark is :",x)
a=x/5
p=300/400*100
print("average is :",a)  
print("percentage is :",p,"%")


# In[7]:


def addition(a,b):
    print("2+3=",a+b)
def sub(a,b):
    print("3-1=",a-b)
def mult(a,b):
    print("2*4=",a*b)
def divi(a,b):
    print("10/2=",a/b)
addition(2,3)
sub(3,1)
mult(2,4)
divi(10,2)


# In[8]:


char="hello"
a=len(char)
print(a)


# In[9]:


num="1236564"
a=num[::-1]
print("reverce of number is :",a)


# In[10]:


a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)


# In[11]:


fact=1
print("numbers are :")
for i in range(1,4):
    print(i)
    fact=fact*i
    i=i+1
print("factorial of 3 is :",fact)    


# In[60]:


Number=10
First=0
Second=1
Sum=0
for Num in range(0, Number):
    print(First, end = '  ')
    Sum=Sum + First
    Next= First + Second
    First=Second
    Second=Next
print("\nThe Sum of Fibonacci Series Numbers:",Sum)


# In[12]:


str1="mayoogha"
if str1.isalpha()==True:
    print("is alphabat")
else:
    print("not alphabat")


# In[13]:


ch="mayppgha"
x="aeiou"
for i in ch:
    if i in x:
        print("is vowel")
    else:
        print("not vowel")


# In[14]:


str1="HELLO"
if str1.isupper()==True:
    print("is uppercase letters")
else:
    print("is lowercase letters")


# In[15]:


str1="welcome"
len(str1)


# In[16]:


str1="malayalam"
str2=str1[::-1]
if str1==str2:
    print("is paliandrom")
else:
    print("not paliandrom")


# In[17]:


x="hello world"
x.replace(" ","_")


# In[18]:


list1=[1,2,3,4]
a=list1[2]
print("The third value is :",a)


# In[19]:


list1=[10,20,30,40]
x=0
for i in list1:
    x=x+i
print("The average is :",x/4)    


# In[20]:


list1=[1,2,3,4,5,6,7]
a=0
b=0
for i in list1:
    if i%2==0:
        a=a+1
    else:
        b=b+1
print("Even numbers are :",a)    
print("Odd numbers are  :",b)


# In[21]:


list1=[10,20,4,36]
a=max(list1)
b=min(list1)
print("The largest number is",a)
print("smallest number is",b)


# In[22]:


list1=[10,20,-2,-3,8]
print("negative numbers in the list")
for i in list1:
    if i<0:
        print(i)


# In[23]:


list1=[1,2,3,4,5,6]
print("list is :",list1)
for i in list1:
    if i%2==0:
        list1.remove(i)
print("remove even numbers in lis :",list1)


# In[24]:


tuple1=(1,2,3,4)
sum=0
for i in tuple1:
    sum=sum+i
print(sum)


# In[25]:


tuple1=(-1,-2,3,4,-9)
print("negative numbers are :")
for i in tuple1:
    if i<0:
        print(i)


# In[26]:


tuple1=('ani','appu','ammu')
print("touple items are :")
for i in tuple1:
    print(i)


# In[27]:


tuple1=('ani','appu','ammu')
len(tuple1)


# In[28]:


tuple1=(1,2,3,4)
x=max(tuple1)
print("large value in tuple is :",x)


# In[29]:


t=(1,2,3,4,5)


# In[30]:


dict1={1:'anu',2:'qmmu',3:'appu'}
print(dict1)


# In[31]:


dict1={1:'anu',2:'qmmu',3:'appu'}
a=3
if a in dict1:
    print("key in dictnory")
else :
    print("key not in dictnory")


# In[32]:


dict1={1:'anu',2:'qmmu',3:'appu'}
len(dict1)


# In[46]:


dict={'anu':10,'ammu':20,'anju':21}
del dict['anu']
print(dict)


# In[43]:


def merge(dict1,dict2):
    return(dict2.update(dict1))
dict1={1:'anu',2:'qmmu',3:'appu'}
dict2={4:'alan',5:'manu'}
merge(dict1,dict2)
print(dict2)


# In[44]:


dict1={1:'anu',2:'qmmu',3:'appu'}
dict2={4:'alan',5:'manu'}
dict1.update(dict2)
print(dict1)


# In[6]:


dict1={'x':1,'y':2,'z':3,'p':4}
x=1
for key in dict1:
    x=x*dict1[key]
print("Multiplying Items in this Dictionary :",x)


# In[7]:


set1={'anu','ammu','appu'}
print(set1)


# In[15]:


set1={1,-2,4,-5,3}
a=0
b=0
for i in set1:
    if i<0:
        a=a+1
    else:
        b=b+1
print("negative numbers are :",a)
print("positive numbers are :",b)


# In[17]:


set1={1,12,4,55,3}
a=max(set1)
print(a)


# In[18]:


set1={1,-2,4,-5,3}
for i  in set1:
    if i<0:
        print(i)


# In[19]:


set1={1,12,4,55,3}
a=min(set1)
print(a)


# In[25]:


set1={1,2,3,4,5,6}
x=0
y=0
for i in set1:
    if i%2==0:
        x=x+i
    else:
        y=y+i
print(x)
print(y)
    


# In[32]:


import numpy as np
arr=np.array([2,3,4,5,7,8])
print('Printing the Array Elements at Even Position :')
print(arr[1:len(arr):2])


# In[34]:


import numpy as np
secLarr=np.array([11, 55, 99, 22, 7, 35, 70])
print("Array Items = ", secLarr)
secLarr.sort()
print("The Second Largest Item in this Array = ", secLarr[len(secLarr)-2])


# In[36]:


import numpy as np
orarr = np.array([10, 20, 10, 30, 40, 30, 70, 11, 19, 40])
print("Original Array= ",orarr)
uniquearr = np.unique(orarr)
print("Unique Array Items=",uniquearr)


# In[43]:


row=4
print("diamand star pattern is")
k=0
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(end=' ')
    while k !=2*i-1:
        print("*",end='')
        k=k+1
    k=0
    print()
k = 2
l = 1
for i in range(1, row):
    for j in range(1, k):
        print(end = ' ')
    k= k+1
    while l<=(2*(row-i)-1):
        print('*', end = '')
        l =l+1
    l=1
    print()


# In[46]:


rows =5
print("X Star Pattern is") 
for i in range(0, rows):
    for j in range(0, rows):
        if(i == j or j==rows - 1 - i):
            print('*',end = '')
        else:
            print(' ',end = '')
    print()


# In[49]:


side =4
print("Square Star Pattern") 
for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()


# In[51]:


rows=4
print("Right Pascals Mirrored Numbers Triangle")
for i in range(rows, 0, -1):
    for j in range(i, rows + 1):
        print(j, end = ' ')
    for k in range(rows - 1, i - 1, -1):
        print(k, end = ' ')
    print()
    
for i in range(2, rows + 1):
    for j in range(i, rows + 1):
        print(j, end = ' ')
    for k in range(rows - 1, i - 1, -1):
        print(k, end = ' ')
    print()


# In[52]:


rows=4
print("Pyramid of Numbers Pattern")
for i in range(1, rows + 1):
    for j in range(rows, i, -1):
        print(end = ' ')
    for k in range(1, i + 1):
        print(i, end = ' ')
    print()


# In[ ]:




