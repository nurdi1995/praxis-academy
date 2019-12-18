#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install jinja2


# In[5]:


from jinja2 import Template
t = Template("Hello {{ something }}!")
t.render(something="World")


# In[6]:


t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
t.render()


# In[ ]:




