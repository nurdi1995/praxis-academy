#!/usr/bin/env python
# coding: utf-8

# # Python Data Structures Tutorial

# ### 1. Float

# In[5]:


# Floats
x = 4.0
y = 2.0

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Returns the quotient
print(x / y)

# Returns the remainder
print(x % y) 

# Absolute value
print(abs(x))

# x to the power y
print(x ** y)


# ### 2. String
# 

# In[10]:


x = 'cake'
y = 'Cookie'
x + '&' + y 


# In[9]:


#repeat
x * 2


# In[11]:


#Range Slicing 
z1 = x[2:]
print(z1)

#Slincing
z2 = y[0] + y[1]
print(z2)


# In[12]:


x = '4'
y = '2'

x+y


# In[13]:


str.capitalize('cookie')


# In[14]:


str1 = "Cake 4 U"
str2 = "404"
len(str1)


# In[16]:


str1.isdigit()


# In[17]:


str2.isdigit()


# In[19]:


str1.replace('4 U', str2)


# In[20]:


str1 = 'cookie'
str2 = 'cook'
str1.find(str2)


# In[22]:


str1 = 'I got you a cookie'
str2  = 'cook'
str1.find(str2)


# ### 3. Boolean
# 

# In[23]:


x = 4
y = 2
x == y


# In[24]:


x>y


# In[25]:


x = 4
y = 2
z = (x==y) # Comparison expression (Evaluates to false)
if z: # Conditional on truth/false value of 'z'
    print("Cookie")


# ### 4. Data Type Conversion

# In[26]:


i = 4.0
type(i)


# ### 5. Implicit Data Type Conversion 

# In[27]:


# A float
x = 4.0 

# An integer
y = 2 

# Divide `x` by `y`
z = x/y

# Check the type of `z`


# ### 6. Explicit Data Type Conversion 

# In[29]:


x = 2
y = "The Godfather: part"
fav_movie = (y) + str(x)

print(fav_movie)


# ### 7. Non-Primitive Data Structures 

# #### a. Array 

# In[30]:


import array as arr

a = arr.array("I",[3,6,9])

type(a)


# #### b. List 

# In[31]:


x = [] #empty list
type(x)


# In[32]:


x1 = [1,2,3]
type(x1)


# In[33]:


x2 = list([1,'apple',3])
type(x2)


# In[34]:


print(x2[1])


# In[35]:


x2[1] = 'orange'
print(x2)


# In[36]:


list_num  = [1,2,45,6,7,2,90,23,435]
list_char = ['c','o','o','k','i','e']

list_num.append(11) ## Add 11 to the list, by default adds to the last position
print(list_num)


# In[37]:


list_num.insert(0, 11)
print(list_num)


# In[38]:


list_char.remove('o')
print(list_char)


# In[39]:


list_char.pop(-2) # Removes the item at the specified position
print(list_char)


# In[40]:


list_num.sort() # In-place sorting
print(list_num)


# In[41]:


list.reverse(list_num)
print(list_num)


# ### c. Arrays versus Lists 

# In[45]:


array_char = array.array("u",["c","a","t","s"])
array_char.tostring()
print(array_char)


# In[47]:


import numpy as np

arr_a = np.array([3,6,9])
arr_b = arr_a/3 ## Performing vectorized (element-wise) operations 
print(arr_b)


# In[48]:


arr_ones = np.ones(4)
print(arr_ones)


# In[49]:


multi_arr_ones = np.ones((3,4)) ## Creating 2D array with 3 rows and 4 columns
print(multi_arr_ones)


# ### d. Stacks 

# In[50]:


stack = [1,2,3,4,5]
stack.append(6) # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 (Top)
print(stack)


# In[51]:


stack.pop() #Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
stack.pop() ## Bottom -> 1 -> 2 -> 3 -> 4 (Top)
print(stack)


# ### e. Queue 

# In[52]:


graph = {"a" : ["c","d"],
         "b" : ["d","e"],
         "c" : ["a","e"],
         "d" : ["a","b"],
         "e" : ["b","c"],       
    
}

def define_edges(graph):
    edges = []
    for vertices in graph:
        for neighbour in graph[vertices]:
            edges.append((vertices, neighbour))
    return edges


print(define_edges(graph))
        


# ### f. Trees 

# In[56]:


class Tree:
    
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right= right
        
    def __str__(self):
        return (str(self.info)+', Left child: ' + str(self.left) + ', Right child: '+str(self.right))
    
tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
    
print(tree)


# ### g. Tuples 

# In[57]:


x_tuple = 1,2,3,4,5
y_tuple = ('c','a','k','e')
x_tuple[0]


# In[58]:


y_tuple[3]
x_tuple[0] = 0 #cannot change value inside a tuple 


# ### h. Dictionary 

# In[63]:


x_dict = {'Edward': 1, 'Jorge':2, 'Prem':3, 'Joe':4}
del x_dict['Joe']
x_dict


# In[64]:


x_dict['Edward'] # Prints the value stored with the key 'Edward'.


# In[65]:


len(x_dict)


# In[69]:


x_dict.keys()


# In[71]:


x_dict.values()


# ### i. Sets 

# In[72]:


x_set = set('CAKE&COKE')
y_set = set('COOKIE')

print(x_set)


# In[74]:


print(y_set) # Single unique 'o'


# In[75]:


print(x_set|y_set) # Unique elements in x_set or y_set or both


# In[76]:


print(x_set & y_set) # Elements in both x_set and y_set


# ### j.file 

# In[77]:


# File modes (2nd argument): 'r'(read), 'w'(write), 'a'(appending), 'r+'(both reading and writing)
f = open('file_name','w')

#Reads entire file
f.read()

#reads one line at a time
f.readline()

# Writes the string to the file, returning the number of char written
f.write('Add this line.') 

f.close()


# In[ ]:




