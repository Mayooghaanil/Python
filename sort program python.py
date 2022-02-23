#!/usr/bin/env python
# coding: utf-8

# In[62]:


# Bubble Sort in Python
arr1=[10,29,3,4,45]
print("elements are :",arr1)
def bubble_sort(arr1):
    for i in range(0,len(arr1)-1):  
        for j in range(len(arr1)-1):
            if(arr1[j]>arr1[j+1]):  
                temp = arr1[j]  
                arr1[j] = arr1[j+1]  
                arr1[j+1] = temp  
    return arr1
print("bubble sorted elements are :",bubble_sort(arr1))                


# In[63]:


# Python Program to Implement Linear Search
def linear_search(arr2,x):
    for i in range(len(arr2)):
        if arr2[i]==x:
            return i
    return -1
arr2=[100,101,102,103,104]
print("elements are :",arr2)
x=104
a=linear_search(arr2,x)
if(a==-1):
    print("sorry")
else:
    print("element idex is :",a)


# In[66]:


# Python Program to Implement Insertion Sort
def insertation_sort(arr3):
    for i in range(0,len(arr3)):
        key=arr3[i]
        j=i-1
        while j>=0 and key<arr3[j] :
            arr3[j+1] = arr3[j]
            j=j-1
            arr3[j+1]=key
arr3=[10,2,30,4,6,23]
insertation_sort(arr3)
print("insertion sort is :")
for i in range(len(arr3)):
    print(arr3[i])


# In[96]:


# Python Program to Implement Merge Sort
def merg(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    left=[0]*n1
    right=[0]*n2
    for i in range(0,n1):
        left[i]=arr[l+i]
    for j in range(0,n2):
        right[j]=arr[m+1+j]
    while i < n1 and j < n2:
         if left[i]<=right[j]:
            arr[k]=left[i]
            i += 1
         else:
            arr[k]=R[j]
            j+= 1
    k += 1
    while i < n1:
        arr[k]=left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k]=right[j]
        j += 1
        k += 1
def mergeSort(arr,l,r):
    if l<r:
        m=l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
arr=[12, 11, 13, 5, 6, 7]
n=len(arr)        
print("given array is :")
for i in range(n):
    print(arr[i])
mergeSort(arr, 0, n-1)
print("Sorted array is :")
for i in range(n):
    print(arr[i])


# In[ ]:




