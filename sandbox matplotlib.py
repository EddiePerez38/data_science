#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import numpy as np


# In[4]:


x = np.linspace(0, 5, 11)
y = x ** 2


# In[5]:


x


# In[6]:


y


# In[8]:


plt.plot(x,y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('First Matplotlib')
plt.show()


# In[10]:


plt.subplot(1,2,1)
plt.plot(x,y, 'r--')
plt.subplot(1,2,2)
plt.plot(y,x, 'g*--')


# In[12]:


#Create Figure (empty canvas)
fig = plt.figure()

#Add set of Axes to figure
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #left, bottom, width, height, (range 0 to 1)

#Plot on that set of axes
axes.plot(x, y,'b')
axes.set_xlabel('Set X Label')
axes.set_ylabel('Set Y Label')
axes.set_title('Set Title')


# In[13]:


# Creates blank canvas
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes

# Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title');


# In[17]:


#Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig, axes = plt.subplots()

#Now use the axes object to add stuff to plot
axes.plot(x, y,'r')
axes.set_xlabel('x')
axes.set_ylabel('x')
axes.set_title('title');


# In[16]:


#Empty canvas of 1 by 2 subplots
fig, axes = plt.subplots(nrows=1, ncols=2)


# In[ ]:




