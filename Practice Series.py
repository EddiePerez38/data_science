#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}


# In[3]:


pd.Series(data=my_list)


# In[4]:


pd.Series(data=my_list, index=labels)


# In[5]:


pd.Series(my_list, labels)


# In[6]:


pd.Series(arr)


# In[7]:


pd.Series(arr,labels)


# In[8]:


pd.Series(d)


# In[9]:


pd.Series(data=labels)


# In[10]:


pd.Series([sum,print,len])


# In[11]:


ser1 = pd.Series([1,2,3,4], index = ['USA', 'GERMANY', 'USSR', 'JAPAN'])


# In[12]:


ser1


# In[13]:


ser2 = pd.Series([1,2,3,4], index = ['USA', 'GERMANY','ITALY','JAPAN'])


# In[14]:


ser2


# In[15]:


ser1['USA']


# In[16]:


ser1 + ser2


# In[ ]:




