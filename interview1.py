#!/usr/bin/env python
# coding: utf-8

# In[39]:


# author: Zachary Wu
# date: 7/27/2021
# version:
# edit history:


import pandas as pd
import matplotlib.pyplot as plt


# # importing data

# In[4]:


data = pd.read_excel('./data_analyst_case_study[2].xlsx')


# In[6]:


data.head()


# # summarizing and cleaning

# In[14]:


print(data.case_type.unique())
print('\n')
print(data.market_sector.unique())


# In[24]:


data.replace(to_replace='netw0rkinggg', value='Networking', inplace=True)
data.replace(to_replace='networking', value='Networking', inplace=True)
print(data.market_sector.unique())

data.fillna('NA', inplace=True)


# In[19]:


data_NPE_Networking = data[(data.case_type == 'NPE') & (data.market_sector == 'Networking')]
n_NPE_Networking = len(data_NPE_Networking.defendant_id.unique())
print(n_NPE_Networking)


# In[26]:


data.groupby(['market_sector', 'case_type']).count()


# # Graphing

# In[35]:


temp = data.groupby(['market_sector', 'case_type']).count().unstack(fill_value=0).stack().reset_index().fillna(0)
n_NPE = temp[temp.case_type=='NPE'].defendant_id
n_OC = temp[temp.case_type=='Operating Company'].defendant_id


# In[61]:


r = range(9)
total = [i+j for i,j in zip(n_NPE, n_OC)]
green = [npe/total*100 for npe,total in zip(n_NPE, total)] 
red = [oc/total*100 for oc,total in zip(n_OC, total)] 

plt.bar(r, green, color='#b5ffb9', edgecolor='white')
plt.bar(r, red, bottom=green, color='#f9bc86', edgecolor='white')

plt.xticks(r, temp.market_sector.unique(), rotation=90)
plt.xlabel('market sector')
plt.legend(['NPE', 'Operating Company'])
plt.title('Number of Defendant by Case Type and Market Sector (100% stack)')

plt.show()


# In[ ]:




