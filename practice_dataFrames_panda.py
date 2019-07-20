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


# In[18]:


#Data frame columns are just a set of series
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


# In[24]:


# Can also frop rows using (this is doesn't permanently drop rows:
df.drop('E',axis=0)


# In[21]:


df


# In[27]:


#Selecting Rows
df.loc['A']


# In[28]:


#Or select based off of a position instead of labels
df.iloc[2]


# In[29]:


#Select a subset of rows
df.loc['B','Y']


# In[30]:


df.loc[['A','B'],['W','Y']]


# In[31]:


df


# In[32]:


df>0


# In[33]:


df[df>0]


# In[36]:


df[df['W']>0]


# In[ ]:




