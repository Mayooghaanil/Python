#!/usr/bin/env python
# coding: utf-8

# In[3]:


# python module example
def add(a,b):
    """The program add teo number and return"""
    result=a+b
    return result


# In[6]:


# import statement example
# to import statement module math
import math
print("The value of pi is :",math.pi)


# In[7]:


# import module by renaming it
import math as m
print("The value of pi is :",m.pi)


# In[8]:


# import only pi from math module
from math import pi
print("The value of pi is :",pi)


# In[11]:


# import all names from the standard module math
# bt using * symbol is not a good programming practice
from math import *
print("The value of pi is :",pi)


# In[13]:


# import from package
import game.level.start


# In[ ]:


# the module containg a function 
import game.level.start.select_difficulity(2)


# In[ ]:


# import the module without the package prefix as follow
from game.level import start
start.select_difficulity(2)


# In[ ]:


# anotherway
from game.level.start import select_difficulity
# now directly call the function
select_difficulity(2)


# In[ ]:




