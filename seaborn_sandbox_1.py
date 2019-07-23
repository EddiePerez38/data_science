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


# In[45]:


flights = sns.load_dataset('flights')


# In[47]:


tips.head()


# In[48]:


#Matrix form for correlation data
tips.corr()


# In[49]:


sns.heatmap(tips.corr())


# In[51]:


sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)


# In[57]:


pvflights = flights.pivot_table(values='passengers', index='month', columns='year')
sns.heatmap(pvflights)


# In[58]:


sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)


# In[59]:


sns.clustermap(pvflights)


# In[60]:


#More options to get the information a little clearer like normailization
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)


# In[61]:


iris = sns.load_dataset('iris')


# In[62]:


iris.head()


# In[63]:


#Just the grid
sns.PairGrid(iris)


# In[64]:


#Then you map the grid
g = sns.PairGrid(iris)
g.map(plt.scatter)


# In[68]:


# Map to upper,lower, and diagonal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# In[69]:


sns.pairplot(iris)


# In[70]:


sns.pairplot(iris, hue='species', palette='rainbow')


# In[71]:


#Just the grid
g = sns.FacetGrid(tips, col='time', row='smoker')


# In[72]:


g = sns.FacetGrid(tips, col='time', row='smoker')
g = g.map(plt.hist, 'total_bill')


# In[74]:


g = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
#Notice how the arguments come after plt.scatter call
g = g.map(plt.scatter, 'total_bill', 'tip').add_legend()


# In[75]:


g = sns.JointGrid(x='total_bill', y='tip', data=tips)


# In[76]:


g = sns.JointGrid(x='total_bill', y='tip', data=tips)
g = g.plot(sns.regplot, sns.distplot)


# In[77]:


sns.lmplot(x='total_bill', y='tip', data=tips)


# In[78]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')


# In[79]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm')


# In[80]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm',
          markers=['o', 'v'],scatter_kws={'s':100})


# In[81]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')


# In[82]:


sns.lmplot(x='total_bill',y='tip',data=tips, row='sex', col='time')


# In[83]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm')


# In[85]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,height=8)


# In[86]:


sns.countplot(x='sex', data=tips)


# In[91]:


sns.set_style('darkgrid')
sns.countplot(x='sex', data=tips)


# In[ ]:




