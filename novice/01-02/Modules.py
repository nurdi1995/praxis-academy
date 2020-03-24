#!/usr/bin/env python
# coding: utf-8

# ## Modules 

# In[1]:



def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# In[7]:


pip install pandas


# In[11]:


pip install fibo


# In[2]:


pip install fibo


# In[4]:


pip install pandas


# In[12]:


pip install fibo


# In[23]:


import fibo


# In[24]:


fibo.fib(1000)


# In[ ]:


fibo.fib2(100)


# ### 1. Lebih lanjut tentang modul 

# In[ ]:


from fibo import fib, fib2
fib(500)


# In[ ]:


from fibo import *
fib(500)


# In[ ]:


import fibo as fib
fib.fib(500)


# In[ ]:


from fibo import fib as fibonacci
fibonacci(500)


# ### 2. Mengoperasikan modul sebagai skrip 

# In[ ]:


python fibo.py <arguments>


# In[ ]:


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))


# In[ ]:


$ python fibo.py 50


# ### 3. modul standard 

# In[36]:


import sys


# In[ ]:


sys.ps1


# In[ ]:



 sys.ps2


# In[37]:



sys.ps1 = 'C> '
print('Yuck!')


# In[38]:


import sys
sys.path.append('/ufs/guido/lib/python')


# ### 3. Fungsi dir() 

# In[40]:


import fibo, sys
dir(fibo)


# In[39]:


dir(sys) 


# In[ ]:


a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()


# In[41]:


import builtins
dir(builtins)


# ### 4. Paket 

# In[ ]:


import sound.effects.echo


# In[ ]:


from sound.effects import echo


# In[ ]:


from sound.effects.echo import echofilter


# ### 5. Mengimport * dari paket 

# In[42]:


__all__ = ["echo", "surround", "reverse"]


# In[43]:


import sound.effects.echo
import sound.effects.surround
from sound.effects import *


# ### 6. Referensi Intra-paket 

# In[44]:


from . import echo
from .. import formats
from ..filters import equalizer


# In[ ]:

#!/usr/bin/env python
# coding: utf-8

# In[3]:


form math import sqrt
print("Sequare root of 16 is", sqrt(16))


# ### 1. The dir function 

# In[7]:


import sys

# get names of attributes in sys module
dir(sys)

# only few entries shown here

# get names of attributes for current module
 dir()
# create a new variable 'a'
 a = 5

dir()

# delete/remove a name
del a

dir()





