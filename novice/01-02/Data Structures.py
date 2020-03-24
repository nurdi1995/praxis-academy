#!/usr/bin/env python
# coding: utf-8

# # Data Struktur

# ### 1. More on list

# In[1]:


fruits  = ['orange','apple','pear','banana','kiwi','apple','banana']


# In[3]:


fruits.count('apple')


# In[4]:


fruits.index('banana') #menghitung index dari list banana


# In[5]:


fruits.index('orange')


# In[7]:


fruits.index('banana',4)  # Find next banana starting a position 4


# In[8]:


fruits.reverse() #Fungsi reversed() berfungsi untuk menghasilkan iterator yang berisi kebalikan dari suatu sequence.


# In[9]:


fruits


# In[10]:


fruits.append('grape') #fungsi append menambahkan grape di list


# In[11]:


fruits


# In[12]:


fruits.append('mango')


# In[13]:


fruits


# In[14]:


fruits.pop()


# ### 2. Using List as Stacks 

# In[23]:


stack = [3,4,5]


# In[24]:


stack.append(6) #menambahkan nilai 6 di tumpukan 


# In[25]:


stack.append(7)


# In[26]:


stack


# In[27]:


stack.pop() #melihat nilai yang baru ditambahkan


# ### 3. Using Lists as Queues

# In[28]:


from collections import deque 


# In[30]:


queue = deque(["Eric","John","Michael"])


# In[31]:


queue.append("Terry")


# In[32]:


queue.append("Graham")


# In[33]:


queue.popleft()


# In[34]:


queue.popleft()


# In[35]:


queue


# ### 4. List Comprehensions

# In[37]:


#List comprehension adalah cara mudah untuk mendefinisikan dan membuat list di Python.
squares = []
for x in range(10):
    squares.append(x**2)
squares


# In[39]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
            
combs


# In[ ]:


vec =[-4, -2, 0, 2, 4] #mebuat list baru 

[x*2 for x in vec]  #list pada variabel vec dikalikan 2 

[x for x in vec if x >=0] # memfilter nilai list >=0

[abs(x) for x in vec] # menerapkan fungsi ke semua element list vec

frestfruit = ['banana','loganberry','passions fruits'] #membuat list

[weapon.strip() for weapon in freshfruit] #Metode strip () mengembalikan salinan string dengan karakter utama dan karakter tambahan dihapus (berdasarkan argumen string yang dilewati).

[(x, x**2) for x in range(6)] #membuat list dengan seperti matrix, 

vec = [[1,2,3],[4,5,6],[7,8,9]] #membuat list dengan variabel vec

[num for elem in vec for num in elem] #membuat list variabel vec dalam 2 baris


# ### 5. Nested List Compresensions

# In[45]:


matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12],]


# In[47]:


[[row[i] for row in matrix] for i in range (4)] #mengelompokkan baris dengan baris kolom dengan kolom dengan range 4


# In[74]:


transposed = []
for i in range(4):
    
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    
transposed


# In[75]:


list(zip(*matrix))


# ### 6. Del Statement

# In[78]:


#menghapus statement di list/ menghapus nilai di list
a = [-1, 1, 66.25, 333, 333, 1234.5] 


# In[79]:


del a [0]
a


# In[81]:


del a[2:4]
a


# In[82]:


del a[:]
a


# ### 6. Tuples and Squences

# In[83]:


t = 12345, 54321, 'hello!'
t[0]


# In[84]:


t


# In[85]:


u = t, (1,2,3,4,5)
u


# In[86]:


v=([1,2,3], [3,2,1])
v


# In[88]:


empty=()
singleton = 'hello', 
len(empty) #mencetak nilai empty


# In[89]:


len (singleton)


# In[90]:


singleton


# ### 7. sets 

# In[93]:


#Fungsi set() berfungsi untuk membuat set dari iterable
basket = {'apple','orange','apple','pear','orange','banana'}


# In[94]:


print(basket)


# In[95]:


'orange' in basket 


# In[96]:


'mango' in basket 


# In[98]:


## Demonstrate set operations on unique letters from two words
a = set ('abracadabra')
b = set ('alacazam')


# In[99]:


a


# In[100]:


b


# In[101]:


a-b # letters in a but not in b


# In[102]:


a|b # letters in a or b or both


# In[103]:


a & b # letters in both a and b


# In[104]:


a ^ b # letters in a or b but not both


# In[106]:


a = {x for x in 'abracadabra' if x not in 'abc'}
a


# ### 8. Dictionaries

# In[117]:


#Dictionary adalah tipe data yang anggotanya terdiri dari pasangan kunci:nilai (key:value). Dictionary bersifat tidak berurut (unordered) sehingga anggotanya tidak memiliki indeks.
tel = {'jack':4098, 'sape' : 4139}
tel['guido']=4127 #menambahkan guido di lsit tel
tel


# In[118]:


tel['jack'] #memanggil nilai dri jack


# In[119]:


del tel['sape']
tel['irv'] = 4127
tel


# In[121]:


list(tel) #menalpilkan daftar list dari tel


# In[123]:


sorted(tel) #mengurutkan list tel


# In[124]:


'guido' in tel


# In[126]:


'jack' not in tel


# In[128]:


dict([('sape',4139),('guido',4127),('jack', 4098)])


# In[130]:


{x: x**2 for x in (2,4,6)} #mengalikan pangkat 2 disetiap listnya


# In[131]:


dict(sape=4139, guido=4127, jack=4098)


# ### 9. Looping Techniques

# In[133]:


knights = {'gallahad':'the pure','robin':'the brave'}
for k, v in knights.items():
    print(k,v)


# In[134]:


for i, v in enumerate(['tic','tac','toe']):
    print(i, v)


# In[137]:


#Untuk mengulang dua atau lebih urutan secara bersamaan, entri dapat dipasangkan dengan fungsi zip ().
questions= ['name','quest','favorite color']
answers  = ['lancelot','the holy grail','blue']
for q, a in zip(questions, answers):
    print('what is your {0}? it is {1}.'.format(q, a))


# In[138]:


#Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi terbalik ().
for i in reversed(range(1,10,2)):
    print(i)


# In[139]:


#Untuk mengulangi urutan dalam urutan diurutkan, gunakan fungsi diurutkan () yang mengembalikan daftar diurutkan baru sambil membiarkan sumber tidak diubah.
basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
    print(f)


# In[142]:


#Terkadang tergoda untuk mengubah daftar saat Anda memutarnya; namun, seringkali lebih mudah dan aman untuk membuat daftar baru.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN')]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
        
filtered_data


# ### 10. More on Condition

# In[143]:


string1, string2, string3 = '','Trondheim','Hammer Dance'
non_null = string1 or string2 or string3
non_null


# ### 11. Comparing Sequences and Other Types 

# In[144]:


(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)


# In[ ]:

#!/usr/bin/env python
# coding: utf-8

# ## Data Structure
# ### 1. Sequence

# In[3]:


#List adalah struktur data yang menyimpan koleksi data terurut, anda dapat menyimpan sequence / rangkaian item menggunakan list.
shooplist = ['apple','mango','carrot','banana']


# In[4]:


shooplist[::1]


# In[5]:


shooplist[::2]


# In[6]:


shooplist[::3]


# In[7]:


shooplist[::-1]


# ### 2. set

# In[8]:


bri = set (['brazil','russia','india'])


# In[9]:


'india' in bri


# In[10]:


'usa' in bri


# In[11]:


bric = bri.copy()
bric.add('china')
bric.issuperset(bri)


# In[12]:


bri.remove('russia')
bri & bric


# In[ ]:




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







