#!/usr/bin/env python
# coding: utf-8

# # 8. Errors and Exceptions

# ### 8.1 Syntax Errors

# In[1]:


while true print ('Hello word')


# ### 8.2 Exceptions

# In[2]:


10 * (1/10)


# In[3]:


4 + spam*3


# In[ ]:


'2' +2


# ### 8.3 Handling Exceptions 

# In[ ]:


while True:
     try:
         x = int(input("Please enter a number: "))
         break
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")


# In[ ]:


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# In[ ]:


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# In[ ]:


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# In[ ]:


try:
   raise Exception('spam', 'eggs')
   except Exception as inst:
       print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
           print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
               x, y = inst.args     # unpack args
               print('x =', x)
               print('y =', y)


# In[ ]:


def this_fails():
     x = 1/0

try:
     this_fails()
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)


# ### 8.4 Raising Exceptions

# In[ ]:


raise NameError('HiThere')


# In[ ]:


try:    
    raise NameError('HiThere')
    except NameError:
         print('An exception flew by!')
            raise


# ### 8.5. User-defined Exceptions
# 

# In[ ]:


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        


# ### 8.6 Defining Clean-up Actions

# In[5]:


try:
        raise KeyboardInterrupt
   finally:
       print('Goodbye, world!')


# In[ ]:


def bool_return():
       try:
           return True
       finally:
       return False


# In[ ]:


def divide(x, y):
       try:
           result = x / y
       except ZeroDivisionError:
           print("division by zero!")
       else:
           print("result is", result)
       finally:
            print("executing finally clause")


# ### 8.7 Predefined Clean-up Actions 

# In[6]:


for line in open("myfile.txt"):
    print(line, end="")


# In[ ]:


with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

