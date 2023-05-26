#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# # Zahoor Ahmed

# In[2]:


import pandas as pd
import requests 


# In[3]:


response = requests.get('https://api.chucknorris.io/jokes/search?query=cat')


# In[4]:


temp_df = pd.DataFrame([response.json])
temp_df


# In[5]:


df = pd.DataFrame()
for i in range(50):
  response = requests.get('https://api.chucknorris.io/jokes/search?query=cat')
  temp_df= pd.DataFrame(response.json()['result'])[['id','created_at','icon_url','updated_at']]
  df = df.append(temp_df)


# In[6]:


df


# In[7]:


df.head()


# In[ ]:




