#!/usr/bin/env python
# coding: utf-8

# In[1]:


# class attribute
class parrot:
    
# instant attribute
    species="bird"

# instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age

# instantiate the parrot class        
blu=parrot("Blu",10)
woo=parrot("Woo",15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributrs
print("{} is {} year old".format(blu.name,blu.age))
print("{} is {} year old".format(woo.name,woo.age))


# In[2]:


# methods
class parrot:
#     instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
#         instance method
    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    def dance(self):
        return "{} is now dancing".format(self.name)
#     instantiate the object
blu=parrot("Blu",10)
# call our instance methods
print(blu.sing("'HAPPY'"))
print(blu.dance())


# In[3]:


# inheritance-using super class
# parent class
class Bird:
    def __init__(self):
        
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swming faster")
# child class
class penguin(Bird):
    def __init__(self):
#         call superclass function
        super().__init__()
        print("penguin is ready")
    def whoisthis(self):
        super().whoisthis()
        print("penguin") 
    def run(self):
        print("Run fast")
peggy=penguin()  
peggy.whoisthis()
peggy.swim() 
peggy.run()


# In[4]:


# eg:with out using super class
# overwrite childclass
class Bird:
    def __init__(self):
        
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swming faster")
class penguin(Bird):
    def __init__(self):
         print("penguin is ready")
    def whoisthis(self):
        print("penguin") 
    def run(self):
        print("Run fast")
peggy=penguin()  
peggy.whoisthis()
peggy.swim() 
peggy.run()


# In[5]:


# encapsulation
class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("selling price: {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice=price
c=computer()
c.sell()
# direct change the price is not possible
c.__maxprice=1000
c.sell()
# using setter function
c.setmaxprice(1000)
c.sell()


# In[6]:


# polymorphism
class parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot cant swim")
class penguin:
    def fly(self):
        print("penguin cant fly")
    def swim(self):
        print("penguin can swim")
# common interface
def flying_test(bird):
    bird.fly()
# instantiate objects
blu=parrot()
peggy=penguin()
# passing the object
flying_test(blu)
flying_test(peggy)


# In[7]:


# polymorphism
class parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot cant swim")
class penguin:
    def fly(self):
        print("penguin cant fly")
    def swim(self):
        print("penguin can swim")
# common interface
# passing common interface and call the function
def flying_test(bird):
    bird.fly()
    bird.swim()
# instantiate objects
blu=parrot()
peggy=penguin()
# passing the object
flying_test(blu)
flying_test(peggy)


# In[8]:


# simple class definition
class MynameClass:
    """This is docstring of a class"""
    pass


# In[9]:


# call the values
class person:
    """This is a person class"""
    age=10
    def greet(self):
        print("hello")
print(person.age)
print(person.greet)
print(person.__doc__)


# In[10]:


# creating an object in pyhton
class person:
    """This is a person class"""
    age=10
    def greet(self):
        print("'Hello'")
harry=person()
# calling objects greet() mehtod
print(person.greet)
print(harry.greet)
harry.greet()


# In[19]:


# normaly initialize all the variables
class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def get_data(self):
        print(f"{self.real}+{self.imag}j")
# creating a new ComplexNumbr object
num1=ComplexNumber(2,3)
# call get_data() method
num1.get_data()
# creating another ComplexNumber object 
# and creating a new attribute 'attr'
num2=ComplexNumber(5)
num2.attr=10
print(num2.real,num2.imag,num2.attr)
# bt c1 object doesnt have attribute 'attr'
print(num1.attr)


# In[ ]:


# deleting attribute and object
class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def get_data(self):
        print(f"{self.real}+{self.imag}j")
num1=ComplexNumber(2,3)
num1.get_data()
# error
del num1.imag
num1.get_data()
del ComplexNumber.get_data
num1.get_data()
c1=ComplexNumber(1,3)
del c1
print(c1)


# In[13]:


# create alass vehicle with instance attribute color,name,speed and functions like speeds,model
# create another class which is inheritted from vehicle with method color
# inharitance
class vehicle:
    def __init__(self,color,name,speed):
        self.color=color
        self.name=name
        self.speed=speed
    def model(self):
        print("The car is new model")
    def speeds(self):
        return "The speed is {}".format(self.speed)
class car(vehicle):
    def colors(self):
        return "The colour is {}".format(self.color)
    def model(self):
        super().model()
        return "The car model is {}".format(self.name)
cars=car("white","i-20",100)
print(cars.model())
print(cars.speeds())
print(cars.colors())


# In[14]:


# build in function is used to check inheritance
# return true if the object is an instnace of the class or other classes derived from it
isinstance(cars,vehicle)


# In[15]:


isinstance(cars,car)


# In[16]:


#  similar to function is used to check inheritance
issubclass(car,vehicle)


# In[17]:


issubclass(vehicle,car)


# In[ ]:




