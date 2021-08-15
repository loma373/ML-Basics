#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


arr=np.ones(10)*5
print(arr)


# In[7]:


arr=np.arange(10,51)
print(arr)


# In[9]:


arr=np.arange(10,51,2)
print(arr)


# In[12]:


arr=np.arange(0,9)
arr1=arr.reshape(3,3)
print(arr1)


# In[17]:


arr=np.random.normal(1,10,25)
print(arr)


# In[20]:


arr=np.arange(0,1,0.01)
print(arr)


# In[23]:


arr=np.linspace(0,1,20)
print(arr)


# In[26]:



arr=np.arange(1,26)
arr1=arr.reshape(5,5)
print(arr1)


# In[30]:


print(arr1[2:,1:])


# In[32]:


print(arr1[:3,1:2])


# In[33]:


#sum of all elements in arr
np.sum(arr1)


# In[39]:


#sum of each column
arr1.sum(axis=0)


# In[40]:


#sum of each row
arr1.sum(axis=1)


# In[ ]:




