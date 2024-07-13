#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://web.archive.org/web/20230908091635/https:/en.wikipedia.org/wiki/List_of_largest_banks"


# In[3]:


resp = requests.get(url)


# In[4]:


p_response = BeautifulSoup(resp.text, "html")


# In[5]:


t_1 = p_response.find("table")


# In[6]:


t_h =t_1.find_all("th")


# In[7]:


t_h


# In[8]:


c_h = [title.text.strip() for title in t_h]


# In[9]:


c_h


# In[10]:


df = pd.DataFrame(columns = c_h)


# In[11]:


df


# In[12]:


column_data = t_1.find_all("tr")[1:]


# In[13]:


column_data


# In[14]:


for row in column_data:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data


# In[15]:


df


# In[16]:


exchange_rates = pd.read_csv(r"E:\Project\E-RATE.csv")


# In[17]:


exchange_rates.drop(['Unnamed: 2'], axis=1, inplace=True)


# In[18]:


exchange_rates


# In[19]:


df["Market cap(US$ billion)"] = pd.to_numeric(df["Market cap(US$ billion)"], errors='coerce')


# In[20]:


df["Market cap(EUR billion)"] = df["Market cap(US$ billion)"] * exchange_rates["Rate"][0]


# In[21]:


df


# In[22]:


df["Market cap(GBP billion)"] = df["Market cap(US$ billion)"] * exchange_rates["Rate"][1]


# In[23]:


df


# In[24]:


df["Market cap(INR billion)"] = df["Market cap(US$ billion)"] * exchange_rates["Rate"][2]


# In[25]:


df


# In[26]:


f_name = "E:\Project\Transformed.csv" 


# In[28]:


df.to_csv(f_name, index=False)


# In[ ]:




