#!/usr/bin/env python
# coding: utf-8

# # UBER TRIP analysis based on start_date and end_date

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib.pyplot as plt
from builtins import list
import matplotlib
matplotlib.style.use('ggplot')

import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


uber_df=pd.read_csv(r"D:\DATA SCIENCE\Uber Data Trip\My Uber Drives - 2016.csv")


# In[4]:


uber_df.head()


# In[5]:


# Remove uncessary data
uber_df = uber_df[:-1]
uber_df.head()


# In[6]:


# fix data types of data columns

def convert_time(column_name):
    y=[]
    for x in uber_df[column_name]:
        y.append(datetime.datetime.strptime(x, "%m/%d/%Y %H:%M"))

    uber_df[column_name] = y


# In[7]:


column_date=uber_df[['START_DATE*','END_DATE*']] 
for x in column_date:
    convert_time(x)


# In[8]:


# check that all data is fixed and ready to work on it
uber_df.info()


# In[9]:


# plot number of trip at each category
x = uber_df['CATEGORY*'].value_counts().plot(kind='bar')


# ### As we notice that the most trips made in business category with huge difference beteewn it and personal category.

# In[10]:


#extract month from start date
count = 0
month=[]
while count < len(uber_df):
    month.append(uber_df['START_DATE*'][count].month)
    count = count+1
uber_df['Month'] = month


# In[11]:


# calculate duration of each trip in minutes
minutes=[]
uber_df['Duration_Minutes'] = uber_df['END_DATE*'] - uber_df['START_DATE*']
uber_df['Duration_Minutes']
for x in uber_df['Duration_Minutes']:
    minutes.append(x.seconds / 60)

uber_df['Duration_Minutes'] = minutes


# In[12]:


# plot number of trips at each month
x = uber_df['Month'].value_counts()
x.plot(kind='bar',figsize=(10,5),color='orange')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Number of trips per Month')


# In[13]:


# I need to see how many trip made at each clock and as you see the clock which has the higest number of trips is 3:00PM
hours = uber_df['START_DATE*'].dt.hour.value_counts()
hours.plot(kind='bar',color='orange',figsize=(10,5))
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.title('Number of trips per hour')


# In[14]:


# see how many trips made by each purpose
purpose_time = uber_df['PURPOSE*'].value_counts()
purpose_time.plot(kind='bar',figsize=(10,5),color='green')


# We need to know the speed of each drive to accomplish each trip, we need to calculate trip in hours at the first and save it into (duration_hours) and then apply speed law speed = distance / time

# In[15]:


# aveverage of each trip according to purpose
purpose = uber_df.groupby('PURPOSE*').mean()
purpose.plot(kind = 'bar',figsize=(15,5))


# In[16]:


# calculate trip speed for each driver
uber_df['Duration_hours'] = uber_df['Duration_Minutes'] / 60
uber_df['Speed_KM'] = uber_df['MILES*'] / uber_df['Duration_hours']
uber_df['Speed_KM']

