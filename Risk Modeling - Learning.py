#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


loan_data_backup = pd.read_csv('loan_data_2007_2014.csv')


# In[3]:


loan_data = loan_data_backup.copy()


# In[4]:


loan_data


# In[6]:


pd.options.display.max_columns = None


# In[7]:


loan_data


# In[8]:


loan_data.head()


# In[9]:


loan_data.columns.values


# In[11]:


loan_data.info()


# ## Preprocessing

# ### Converting Objects to Interger

# #### Emp_Length

# In[17]:


loan_data['emp_length'].unique()


# In[28]:


loan_data['emp_length_int'] = loan_data['emp_length'].str.replace('\+ years','')
loan_data['emp_length_int'] = loan_data['emp_length_int'].str.replace('< 1 year',str(0))
loan_data['emp_length_int'] = loan_data['emp_length_int'].str.replace('n/a',str(0))
loan_data['emp_length_int'] = loan_data['emp_length_int'].str.replace(' years','')
loan_data['emp_length_int'] = loan_data['emp_length_int'].str.replace(' year','')


# In[29]:


loan_data['emp_length_int'].unique()


# In[30]:


loan_data['emp_length_int'] = pd.to_numeric(loan_data['emp_length_int'])


# In[32]:


type(loan_data['emp_length_int'][0])


# #### Term

# In[33]:


loan_data['term'].unique()


# In[37]:


loan_data['term_int'] = loan_data['term'].str.replace(' ','')
loan_data['term_int'] = loan_data['term_int'].str.replace('months','')


# In[38]:


loan_data['term_int'].unique()


# #### Earliest_cr_line and Loan Issue data

# In[ ]:




