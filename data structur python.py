#!/usr/bin/env python
# coding: utf-8

# In[1]:


cars = ["Ford", "Volvo", "BMW"]
# a=cars.pop(1)
# print(a)
cars.index("Ford")


# In[2]:


# array
cars = ["Ford", "Volvo", "BMW"]
cars[0]


# In[3]:


# Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
print(cars)
print(type(cars))


# In[4]:


# NumPy is used to work with arrays.The array object in NumPy is called ndarray
import numpy as np
value= np.array([1, 2, 3, 4, 5])
print(value)
print(type(value))


# In[5]:


#  array(data type, value list):- This function is used to create an array
import array
arr = array.array('i', [1, 2, 3])
for a in arr:
    print(a)
print(type(arr))


# In[6]:


# Python Program to Split the array and add the first part to the end
arr1=[1,2,3,4,5,6]
print("Old array :",arr1)
x = arr1[-4:]
y=arr1[:2]
print("aranged array :",x+y)


# In[7]:


# Program to calculate average of an array
import numpy as ar
nums=ar.array([5,10,15,20])
l=len(nums)
print(nums)
for i in nums:
    sum=i+i
print("Average is :",sum/l)


# In[8]:


# Program to find the smallest element of an array
arr1=[100,442,53,472]
small=min(arr1)
print("The smallest element is :",small)


# In[9]:


# Python Program to find largest element in an array
arr1=[10,203,39,4]
larg=max(arr1)
print("The large element is :",larg)


# In[10]:


# Program to copy an array to another array in reverse
arr1=[1,2,3,4,5,6]
print("The array :",arr1)
x = arr1[::-1]
print("Reverse is :",x)


# In[11]:


# Program to find the second largest element of an array
import numpy as np
arr1=np.array([11, 55, 99, 22, 7, 35, 70])
print("The array is :",arr1)
arr1.sort()
num=arr1[len(arr1)-1]
print("The second largest element is :",num)


# In[12]:


# Write a Python program to get the length of an array.
import numpy as np
arr=np.array(['ammu','appu','akku','anju','alan'])
print("Array length is :",len(arr))


# In[13]:


# create an array of 5 integers and display the array items. access individual element through indexes
element=[10,11,12,13,14]
for i in element:
    print(i)
element[0]


# In[14]:


# program to reverse the order of the items in the array
arr1=['name','age','number','mark']
print(arr1)
a=arr1[::-1]
print(a)


# In[15]:


# Python program to print the elements of an array present on even and odd position
arr=[0,1,2,3,4,5,6,7]
print("Odd numbers are")
for i in range(1,8,2):
    print(i)
print("Even numbers are")
for n in range(0,7,2):
    print(n)


# In[28]:


# Python program to print the number of elements present in an array
import numpy as ar
nums=ar.array(['apple','mango','orange'])
print("number of elements present in an array :",len(nums))


# In[26]:


# Python program to print the duplicate elements of an array
arr=[1,2,3,2,4,5,4,5]
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] == arr[j]):
            print(arr[i])


# In[37]:


# Converting Array to List
import numpy as np
valu=np.array([10,20,30,40])
print(type(valu))
a=list(valu)
# a=valu.tolist()
print(type(a))


# In[49]:


# Program to divide one array into two arrays
arr=[10,20,30,40,50]
print(arr)
newarr=np.array_split(arr,2)
print(newarr)


# In[53]:


# program to append a new item to the end of the array
arr=[10,20,30,40]
print("Old array :",arr)
arr.append(100)
print("New array :",arr)


# In[5]:


# Write a Python program to insert a new item before the second element in an existing array.
arr=[1,2,3,4,5]
print(arr)
arr.insert(1,100)
print("insert a new item before the second element")
print(arr)


# In[ ]:




