#!/usr/bin/env python
# coding: utf-8

# In[4]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


tips = sns.load_dataset('tips')


# In[6]:


tips.head()


# In[7]:


sns.distplot(tips['total_bill'])


# In[8]:


sns.distplot(tips['total_bill'],kde=False,bins=30)


# In[9]:


sns.jointplot(x='total_bill', y='tip',data=tips,kind='scatter')


# In[10]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')


# In[11]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[12]:


sns.pairplot(tips)


# In[13]:


sns.pairplot(tips,hue='sex',palette='coolwarm')


# In[14]:


sns.rugplot(tips['total_bill'])


# In[15]:


# Don't worry about understanding this code!
# It's just for the diagram below
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min,x_max,100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)


# In[16]:


# To get the kde plot we can sum these basis functions.

# Plot the sum of the basis function
sum_of_kde = np.sum(kernel_list,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")


# In[17]:


sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])


# In[18]:


sns.kdeplot(tips['tip'])
sns.rugplot(tips['tip'])


# In[19]:


sns.barplot(x='sex', y='total_bill', data=tips)


# In[20]:


sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)


# In[21]:


sns.countplot(x='sex', data=tips)


# In[22]:


sns.boxplot(x='day', y='total_bill', data=tips, palette="rainbow")


# In[24]:


sns.boxplot(data=tips, palette='rainbow', orient='h')


# In[25]:


sns.boxplot(x='day', y='total_bill', hue='smoker', data=tips, palette='coolwarm')


# In[26]:


sns.violinplot(x='day', y='total_bill', data=tips, palette='rainbow')


# In[29]:


sns.violinplot(x='day', y='total_bill', data=tips, hue='sex',  palette="Set1")


# In[30]:


sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True, palette="Set1")


# In[31]:


sns.stripplot(x='day', y='total_bill', data=tips)


# In[32]:


sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)


# In[33]:


sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', palette='Set1')


# In[37]:


sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',dodge=True)


# In[38]:


sns.swarmplot(x='day', y='total_bill', data=tips)


# In[40]:


sns.swarmplot(x='day', y='total_bill', data=tips, hue= 'sex', palette='Set1', dodge=True)


# In[41]:


sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)


# In[43]:


sns.catplot(x='sex', y='total_bill', data=tips, kind='bar')


# In[ ]:




