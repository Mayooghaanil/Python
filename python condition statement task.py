#!/usr/bin/env python
# coding: utf-8

# In[58]:


# write a python program to find those numbers which are divisible by 7 and multiple by 5
lower=1500
upper=2700
for i in range (lower,upper+1):
    if(i%7==0 and i%5==0):
        print(i)


# In[33]:


for i in range(0, 5):
    for j in range(0, i+1):
        print("* ",end="")
    print()
for i in range(0,5):
    for j in range(0,4-i):
        print("* ",end="")
    print()


# In[57]:


list1=[1,2,3,4,5,6,7]
list2=[]
list3=[]
for i in list1:
    if (list1[i-1]%2==0):
        list2.append(i)
    else:
        list3.append(i)
print("Even numbers are :",list2)
print("Odd numbers are :",list3)


# In[ ]:




