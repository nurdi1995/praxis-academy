#!/usr/bin/env python
# coding: utf-8

# In[2]:


#First-Class Functions
def greeting():
    print("Hello Word!")

greeting()
    


# In[14]:


def perkalian(kali):
    hasil = kali * kali
    return hasil


print ("Luas persegi: %d" % perkalian(5))


# In[17]:


def halo(nama):
    print('Halo %s!' % nama)


# In[21]:


#Passing Functions as Parameters

def formalGreeting():
    print("How are you?")
    
def casualGreeting():
    print("What's up?")

def greet(type, greetFormal, greetCasual):
    if (type=='formal'):
        greetFormal()
    elif (type=='casual'):
        greetCasual()
        
greet('casual', formalGreeting, casualGreeting )


# In[24]:


arr1 =[1,2,3]
arr2=[]

for i in arr1:
    arr2.append(i*2)
print(arr2)


# In[27]:


birthYear = [1975, 1997, 2002, 1995, 1985]
ages=[]

for i in birthYear:
    age = 2018-i
    ages.append(age)
    
print(ages)
    


# In[36]:


#With Higher-order function map
birthYear = [1975, 1997, 2002, 1995, 1985]
ages =map(lambda i: 2018 - i, birthYear)
print(list(ages))


# In[12]:


persons ={
          "1":{
              'name': 'Peter', 'age': '16'
          },
          "2":{
              'name': 'Mark', 'age': 18
          },
          "3":{
              'name': 'John', 'age': 27
          },
          "4":{
              'name': 'Jane', 'age': 14
          },
          "4":{'name': 'Tony', 'age':24
              }
         }

fullAge=[]


[v for v in persons.values() if 18 in v.values()]
        

    


# In[21]:


persons ={
          "1":{
              'name': 'Peter', 'age':16
          },
          "2":{
              'name': 'Mark', 'age': 18
          },
          "3":{
              'name': 'John', 'age': 27
          },
          "4":{
              'name': 'Jane', 'age': 14
          },
          "4":{'name': 'Tony', 'age':24
              }
         }

fullAge=[]


# In[22]:



[v for v in persons.values() if 18 in v.values()]


# In[23]:


list(filter(lambda x: x if x['age'] >= 18  else None, persons.values()))


# # EXAMPLE
# 

# In[26]:


import functools
arr = [5, 7, 1, 8, 4]
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,arr)) 


# In[ ]:


print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,arr)) 


# In[25]:


strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'C']

def mapForEach(arr):
    newArray = []
    for i in range (len(strArray)):
        newArray.append(len(arr[i]))
    return newArray
        
    
lenArray = mapForEach(strArray)

print(lenArray)


# In[ ]:




