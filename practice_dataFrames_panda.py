#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from numpy.random import randn
np.random.seed(101)


# In[3]:


df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())


# In[4]:


df


# In[6]:


df['W']


# In[8]:


df[['W','Z']]


# In[9]:


df.W


# In[10]:


type(df["W"])


# In[11]:


#Creating new columns
df['new'] = df["W"] + df["Y"]


# In[12]:


df


# In[13]:


#Removing columns
df.drop("new", axis=1)


# In[14]:


#Not inplace unless specified!
df


# In[16]:


df.drop('new',axis=1,inplace=True)


# In[17]:


df


# In[ ]:




