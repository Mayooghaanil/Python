#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None


# In[2]:


# Display Linked List in Reverse
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print ("Given Linked List :")
llist.printList()
llist.reverse()
print ("Reversed Linked List :")
llist.printList()


# In[12]:


# Implement traversal in linked list
class Node:
    def __init__(self,val,nxt):
        self.val = val
        self.nxt = nxt  
def traversal(node):
    if not node.nxt:
        print(node.val)
        return 
    traversal(node.nxt)
    print(node.val)
a=int(input("Enter the first number : "))
b=int(input("Enter th second number : "))
c=int(input("Enter th third number : "))
d=int(input("Enter the fourth number : "))
n0 = Node(a,None)
n1 = Node(b,n0)
n2 = Node(c,n1)
n3 = Node(d,n2)
traversal(n3)


# In[ ]:




