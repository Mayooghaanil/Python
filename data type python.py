#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=10.44
print(type(a))


# In[3]:


f=1.2e3
print(f)


# In[4]:


a=0b1111+2j
print(a)


# In[5]:


a=15+0b1111j
print(a)


# In[ ]:


x=10+20j
print(x)
type(x)
y=12.5+2.3j
print(x+y)
print(x-y)
x.real
x.imag


# In[ ]:


a="Hello world"
print(type(a))


# In[71]:


num=2
factorial=1
if (num < 0):
    print("negative number")
elif (num == 0):
    print("factorial is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
        print("The factorial of",num,"is",factorial)


# In[ ]:


num=int(input("Enter a number"))
factorial=1
if(num<0):
    print("negative number")
elif(num==1):
    print("factorial is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print(factorial)


# In[ ]:


a=True
a


# In[ ]:


a=true
a


# In[ ]:


True+True


# In[ ]:


True+False


# In[ ]:


False+False


# In[ ]:


s='''Hell....
world'''
print(s)


# In[ ]:


s=john
print(s)


# In[ ]:


s="mayoogha"
print(s)


# In[ ]:


s='mayoogha'
print(s)


# In[ ]:


x=[10,20,30,40]
b=bytes(x)
type(b)


# In[ ]:


x=[10,20,30,40]
b=bytes(x)
b[0]


# In[27]:


x=[10,20,30,40]
b=bytes(x)
b[1]


# In[28]:


x=[10,20,30,40]
b=bytes(x)
b[0:3]


# In[29]:


x=[10,256,258,7]
b=bytes(x)


# In[12]:


x=[10,20,30,40]
b=bytes(x)
b[0]=30
print(b)


# In[30]:


x=[10,20,30,40]
b=bytearray(x)
type(b)


# In[16]:


b[0]=15
for i in b: print(i)


# In[18]:


a=[10,10.5,'anu',20,20]
print(a)


# In[19]:


a[0]=20
print(a)


# In[21]:


a=(10,20,'ammu',4.3)
print(a)


# In[23]:


a[2]


# In[24]:


a[0]=3


# In[39]:


r=range(10)
print(r)


# In[40]:


r[0]


# In[41]:


r[0:3]


# In[42]:


r[0]=33


# In[43]:


for i in r: print(i)


# In[45]:


r=range(10,30)
r


# In[46]:


r[5]


# In[48]:


for i in r: print (i)


# In[50]:


r=range(10,40,5)
for i in r: print(i)


# In[51]:


for i in range(2,5,8): print(i)


# In[52]:


for i in range(8,1,-3):print(i)


# In[64]:


s={10,20,30,10,20}
print(s)


# In[56]:


s[0]


# In[65]:


s.add('anu')
print(s)


# In[66]:


s.remove(20)
print(s)


# In[68]:


s={10,20,30,40}
fs=frozenset(s)
type(fs)


# In[69]:


print(fs)


# In[70]:


fs.add(50)


# In[1]:


d={100:'ammu',200:'appu'}
type(d)


# In[2]:


print(d)


# In[4]:


s={}
type(s)


# In[10]:


s=set()
type(s)
# print(s)


# In[26]:


d={}
d[100]='john'
d[200]='john'
d['tasty']='pizza'
print(d)


# In[14]:


d[100]='smith'
print(d)


# In[17]:


a=None
print(a)


# In[ ]:





# In[ ]:




