#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


USAhousing = pd.read_csv("USA_Housing.csv")


# In[5]:


USAhousing.head()


# In[6]:


USAhousing.info()


# In[7]:


USAhousing.columns


# In[8]:


sns.pairplot(USAhousing)


# In[9]:


sns.distplot(USAhousing["Price"])


# In[10]:


sns.heatmap(USAhousing.corr())


# In[14]:


X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
Y = USAhousing['Price']


# In[15]:


from sklearn.model_selection import train_test_split


# In[16]:


#What is random state in this case
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


# In[17]:


from sklearn.linear_model import LinearRegression


# In[18]:


lm = LinearRegression()


# In[20]:


lm.fit(X_train,y_train)


# In[22]:


print(lm.intercept_)


# In[24]:


coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
coeff_df


# In[25]:


predictions = lm.predict(X_test)


# In[26]:


plt.scatter(y_test,predictions)


# In[27]:


sns.distplot((y_test-predictions),bins=50);


# In[28]:


from sklearn import metrics


# In[34]:


print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print("MSE:", metrics.mean_squared_error(y_test, predictions))
print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, predictions)))


# In[ ]:




