#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[2]:


init_notebook_mode(connected=True)


# In[3]:


import pandas as pd


# In[4]:


data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['text1','text2','text3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})


# In[5]:


layout = dict(geo = {'scope': 'usa'})


# In[6]:


choromap = go.Figure(data = [data], layout = layout)


# In[7]:


iplot(choromap)


# In[9]:


df = pd.read_csv('2011_US_AGRI_Exports')
df.head()


# In[14]:


data = dict(type='choropleth',
            colorscale = 'RdBu',
            locations = df['code'],
            z = df['total exports'],
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"Millions USD"}
            )


# In[15]:


layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )


# In[16]:


choromap = go.Figure(data = [data],layout = layout)


# In[17]:


iplot(choromap)


# In[20]:


df = pd.read_csv('2014_World_GDP')
df.head()


# In[21]:


data = dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorbar = {'title' : 'GDP Billions US'},
      ) 


# In[28]:


layout = dict(
    title = '2014 Global GDP',
    geo = dict(
        showframe = False,
        projection = {'type':'equirectangular'}
    )
)


# In[30]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)


# In[ ]:




