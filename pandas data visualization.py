#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
df3=pd.read_csv('df3.csv')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df3.info()


# In[5]:


df3.head()


# In[6]:


df3.plot.scatter(x='a',y='b',c='red',s=50,figsize=(12,3))


# In[7]:


df3['a'].plot.hist()


# In[8]:


plt.style.use('ggplot')


# In[9]:


df3['a'].plot.hist(alpha=0.5,bins=25)


# In[10]:


df3[['a','b']].plot.box()


# In[11]:


df3['d'].plot.kde()


# In[12]:


df3['d'].plot.density(lw=5,ls='--')


# In[15]:


df3.ix[0:30].plot.area(alpha=0.4)


# In[16]:


f=plt.figure()
df3.ix[0:30].plot.area(alpha=0.4,ax=f.gca())
plt.legend(loc='center left',bbox_to_anchor=(1.0,0.5))
plt.show()


# In[ ]:




