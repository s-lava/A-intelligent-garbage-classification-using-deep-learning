#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


d = {'country':['France','Spain','Germany','spain','Germany','France','Spain','France','Germany','France'],
     'Age':[44,27,30,38,40,35,np.nan,48,50,37],
     'salary':[72000,48000,54000,61000,np.nan,58000,52000,79000,83000,67000],
     'purchased':['No','yes','No','No','yes','yes','no','yes','no','yes']}
d

            


# In[4]:


df1=pd.DataFrame(d)


# In[5]:


df1


# In[7]:


df1['Age'].mean()


# In[10]:


df1['Age'] = df1['Age'].fillna(df1['Age'].mean())


# In[9]:


df1['salary'].mean()


# In[11]:


df1['salary']=df1['salary'].fillna(df1['salary'].mean())


# In[12]:


df1


# In[13]:


df1 = df1.drop_1()


# In[14]:


df1 = df1.drop(3)


# In[15]:


df1


# In[19]:


df1.loc[10]=['india',79,25000000,'yes']


# df1

# In[20]:


df1


# In[21]:


df1


# In[ ]:




