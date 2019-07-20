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


# In[39]:


df[df['W']>0]['Y']


# In[40]:


df[df['W']>0][['Y','X']]


# In[45]:


df[(df['W']>0) & (df['Y'] > 1)]


# In[46]:


df


# In[47]:


#Reset to default 0,1...n index
df.reset_index()


# In[50]:


newind = 'CA NY WY OR CO'.split()


# In[52]:


df['States'] = newind


# In[53]:


df


# In[54]:


df.set_index('States')


# In[55]:


df


# In[56]:


df.set_index('States',inplace=True)


# In[57]:


df


# In[58]:


#The next section is related to multi index and index Hierarchy
# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[59]:


hier_index


# In[61]:


df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df


# In[65]:


df.loc['G1'].loc[1]


# 

# In[67]:


df.index.names


# In[68]:


df.index.names = ['Groups','Num']


# In[69]:


df


# In[70]:


df.xs("G1")


# In[71]:


df.xs(['G1',1])


# In[72]:


df.xs(1,level="Num")


# In[ ]:




