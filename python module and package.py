#!/usr/bin/env python
# coding: utf-8

# In[1]:


# value of 4 to the power of 3
import math
print("The square root is :",math.sqrt(25))


# In[2]:


# factorial of a number
import math as m
print("The factorial is :",m.factorial(4))


# In[3]:


# display current date
from datetime import date
today=date.today()
print("The current date is :",today)


# In[4]:


# current date and time
from datetime import datetime
today=datetime.now()
print("The current date and time is :",today)


# In[5]:


# current time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("The current date is :",current_time)


# In[6]:


# find lowest and heighst value
list1=[10,11,12,13,14]
a=max(list1)
b=min(list1)
print("The largest value is :",a)
print("The smellest value is :",b)


# In[7]:


# find absalute value
a=int(input("Enter the number :"))
print("The absalute value is :",abs(a))


# In[3]:


# value of 4 to the power 3
from math import pow
print("The power is :",pow(4,3))


# In[ ]:




