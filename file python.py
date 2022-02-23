#!/usr/bin/env python
# coding: utf-8

# In[1]:


# open file in curretnt director
f=open("kjxcc.txt")
f


# In[2]:


# specifying full path
f=open("D://hospital registration.txt")
f


# In[3]:


# equivalent to 'r' or 'rt'
f=open("kjxcc.txt")


# In[4]:


# write in text mode
f=open("kjxcc.txt",'w')
f


# In[5]:


# read and write binary mode
# f=open("img.bmp",'r+b')
f=open("D://manimg.jpg",'r+b')
f


# In[6]:


# encoding
f=open("kjxcc.txt",mode="r",encoding="utf-8")


# In[7]:


# close file in python
# The method is not entirely safe
f=open("kjxcc.txt",mode="r",encoding="utf-8")
    # perfornm file operations
f.close()


# In[8]:


# safe way to use a try...finally block
try:
    f=open("kjxcc.txt",encoding='utf-8')
    # perfornm file operations
finally:
    f.close()


# In[9]:


# it is done in internally
# with use to close file
with open('kjxcc.txt','w',encoding='utf-8') as file:
    file.write('hello world !')


# In[10]:


# overwriting
with open('kjxcc.txt','w',encoding='utf-8') as file:
    file.write('welcome')


# In[11]:


# write in a file txt
with open('test.txt','w',encoding='utf-8')as f:
    f.write("My first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
f


# In[12]:


f=open("test.txt",'r',encoding='utf-8')


# In[13]:


f.read(4)


# In[14]:


f.read(4)


# In[15]:


f.read()


# In[16]:


# further reading return empty string
f.read()


# In[17]:


# get the current file position
f.tell()


# In[18]:


f.seek(0)


# In[19]:


# read the entire file
print(f.read())


# In[20]:


# read a file line by line using for loop
f=open("test.txt",'r',encoding='utf-8')
for line in f:
    print(line, end= '')


# In[21]:


f.readline()


# In[34]:


f.readlines()


# In[ ]:





# In[ ]:




