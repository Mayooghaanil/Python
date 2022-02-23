#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import to os
import os


# In[2]:


# return current working directory
os.getcwd()


# In[3]:


# return current working directory in bytes
os.getcwdb()


# In[4]:


# print current working directory
print(os.getcwd())


# In[5]:


# change directory
os.chdir('D:\Screenshots')
print(os.getcwd())


# In[6]:


# All files inside a current working directory
os.listdir()


# In[7]:


# All files inside C directory
os.listdir('C:\\')


# In[8]:


# to make a new directory
os.mkdir('test')


# In[9]:


os.listdir()


# In[10]:


# rename the directory
os.rename('test','new_name')


# In[11]:


os.listdir()


# In[13]:


# remove file
os.remove('flower.jpg')
os.listdir()


# In[14]:


# remove a empty directory
os.rmdir('new_name')


# In[15]:


os.listdir()


# In[2]:


# remove a non empty directory
import shutil
shutil.rmtree('D:\Screenshots')
os.listdir()


# In[ ]:





# In[ ]:




