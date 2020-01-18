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




