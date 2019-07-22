#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[26]:


df = pd.read_html('https://finance.yahoo.com/commodities')


# In[28]:


df[0]


# In[29]:


new_df=df[0]


# In[30]:


new_df.pivot_table(columns=['Name', 'Last Price'])


# In[31]:


new_df.describe()


# In[33]:


new_df.Name


# In[37]:


new_df.loc[[1,20],['Name', 'Last Price']]


# In[38]:


new_df[new_df['Last Price']>100]


# In[39]:


new_df.dropna(axis=1)


# In[ ]:




