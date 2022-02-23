#!/usr/bin/env python
# coding: utf-8

# In[1]:


# syntax error
if a<3


# In[2]:


# logical error
1/0


# In[4]:


# logical error
open("hii.txt")


# In[5]:


# python build in exceptions
print(dir(locals()['__builtins__']))


# In[13]:


# in pythpn exception handling usinsg a try statement
# import module sys ot get the type of exception
import sys
randomlist=['a',0,2]
for entry in randomlist:
    try:
        print("The entry is",entry)
        r=1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occurred.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)


# In[17]:


# multiple exceptions in an exceptions
try:
#     do somthing
    pass
except ValueError:
#     handle ValueError exception
    pass
except (TypeError,ZeroDivisionError):
#    handle ValueError exception
#    TypeError and ZeroDivisionEror
    pass
except:
#     handle all other exceptions
    pass


# In[19]:


# optionaly pass values to theexception to clarify why that exception was raised
# raise KeyboardTnterrupt


# In[21]:


# raise Memoryerror("This is an argument")


# In[25]:


try:
    a=int(input("Enter a positive integer"))
    if a<=0:
        raise ValueError("This is not a positive number!")
except ValueError as ve:
    print(ve)    


# In[29]:


# python try else clause
# program to print the reciprocal of even numbers
try:
    num=int(input("Enter a number"))
    assert num%2==0
except:
    print("Not an even number!")
else:
    reciprocal=1/num
    print(reciprocal)


# In[1]:


# pyhton file finally
try:
    f=open("kjxcc.txt",encoding='utf=8')
#     perform file operation
finally:
    f.close()


# In[ ]:




