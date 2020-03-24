#!/usr/bin/env python
# coding: utf-8

# ## Input and output 

# ### 1. Fancier Output Formatting 

# In[2]:


year = 2016
event = 'Referendum'
f' Results of the {year} {event}'


# In[3]:


yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'


# In[12]:


s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))


# ### 2. Formatted String Literals 

# In[13]:


import math
print(f'The value of pi is approximately {math.pi:.3f}.')


# In[15]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
        print(f'{name:10} ==> {phone:10d}')


# In[16]:


animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')


# ### 3. The String format() Method 

# In[17]:


print('We are the {} who say "{}!"'.format('knights', 'Ni'))


# In[18]:


print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))


# In[19]:


print('This {food} is {adjective}.'.format(
           food='spam', adjective='absolutely horrible'))


# In[21]:


print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))


# In[2]:


table = {'Sjoerd': 4127, 'jack': 4098, 'Dcab': 8637678}
 print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
          'Dcab: {0[Dcab]:d}'.format(table))


# In[3]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
 print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678


# In[5]:


for x in range (1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    


# ### 4. Manual String Formatting

# In[6]:


for x in range (1,11):
     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     # Note use of 'end' on previous line
     print(repr(x*x*x).rjust(4))


# In[8]:


'12'.zfill(5)


# In[9]:


'-3.14'.zfill(-7)


# In[10]:


'3.14159265359'.zfill(5)


# ### 5. Old String formatting 

# In[11]:


import math 
print('The value of pi is approximatelt %5.3f.' %math.pi)


# ### 6. Reading and Writting Files

# In[12]:


f = open ('workfile','w')


# In[14]:


with open('workfile') as f:
     read_data = f.read()
    f.closed


# In[ ]:


f.close()
f.read()


# ### 7. Methods of File Objects

# In[15]:


f.read()


# In[ ]:


f.readline()


# In[16]:


for line in f:
    print (line, end='')


# In[17]:


f.write('This is a test\n')


# In[18]:


value = ('the answer', 42)
s= str(value)
f.write(s)


# In[19]:


f = open ('workfile', 'rb+')
f.write(b'0123456789abcdef')


# In[20]:


f.seek(5)


# In[21]:


f.read(1)


# In[22]:


f.seek(-3,2)


# In[23]:


f.read(1)


# ### 8. Saving structured data with json

# In[24]:


import json
json.dumps([1,'simple','list'])


# In[ ]:




