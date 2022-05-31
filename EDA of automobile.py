#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


auto=pd.read_csv(r"C:\Users\MAMTA THAKUR\Downloads\Automobile_data.csv")


# In[5]:


auto.head()


# In[14]:


cols=['symboling','normalized_losses','make','fuel_type','aspiration','num_of_doors','body_style','drive_wheels_engine','location','wheel_base','length','width','height','curb_weight','engine_type','num_of_cylinders','engine_size','fuel_system','bore','stroke','compression_ratio','horsepower','peak_rpm','city_mpg','highway_mpg','price']


# In[16]:


auto.columns=cols


# In[17]:


auto.head()


# In[18]:


auto.isnull().sum()


# In[19]:


auto.info()


# In[20]:


#Checking for wrong entries like symbols -,?,#,*,etc.
for col in auto.columns:
    print('{} : {}'.format(col,auto[col].unique()))


# In[24]:


for col in auto.columns:
    auto[col].replace({'?':np.nan},inplace=True)


# In[25]:


auto.head()


# In[26]:


auto.isnull().sum()


# In[27]:


sns.heatmap(auto.isnull(),cbar=False,cmap='viridis')


# In[28]:


num_col = ['normalized_losses', 'bore',  'stroke', 'horsepower', 'peak_rpm','price']
for col in num_col:
    auto[col]=pd.to_numeric(auto[col])
    auto[col].fillna(auto[col].mean(), inplace=True)
auto.head()


# In[29]:


plt.figure(figsize=(10,10))
sns.heatmap(auto.corr(),cbar=True,annot=True,cmap='Blues')


# In[30]:


plt.figure(figsize=(10,10))
plt.scatter(x='horsepower',y='price',data=auto)
plt.xlabel('Horsepower')
plt.ylabel('Price')


# In[31]:


sns.histplot(auto.horsepower,bins=10)


# In[32]:


plt.figure(figsize=(10,10))
plt.scatter(x='engine_size',y='price',data=auto)
plt.xlabel('Engine size')
plt.ylabel('Price')


# In[33]:


plt.figure(figsize=(10,10))
plt.scatter(x='highway_mpg',y='price',data=auto)
plt.xlabel('Higway mpg')
plt.ylabel('Price')


# In[34]:


#Unique values in num_of_doors
auto.num_of_doors.value_counts()


# In[35]:


sns.boxplot(x='price',y='num_of_doors',data=auto)


# In[ ]:




