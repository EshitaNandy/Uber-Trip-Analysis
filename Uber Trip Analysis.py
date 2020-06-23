#!/usr/bin/env python
# coding: utf-8

# # Importing Necessary Libraries

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn


# ## Loading CSV file into memory

# In[2]:


data = pandas.read_csv(r"D:\DATA SCIENCE\Uber Data Trip\RawUberData.csv")


# In[3]:


data.head()


# ## Covert Date Time 

# In[4]:


data ['Date/Time'] = data ['Date/Time'].map(pandas.to_datetime)


# In[6]:


data.head()


# In[7]:


def get_dom(dt):
    return dt.day
data['dom'] = data['Date/Time'].map(get_dom)


# In[8]:


data.head()


# In[13]:


def get_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)

data.tail()


# ## ANALYSIS

# ## Analysis of the DoM

# In[25]:


hist(data.dom, bins=30, rwidth=.8, color='#800000', range=(0.5, 30.5))
xlabel('Date of the month')
ylabel('Frequency')
title('Frequency by DoM - uber - Apr 2014')


# In[16]:


#for k, rows in data.groupby('dom'):
#print((k, len(rows)))
 
def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date


# In[17]:


bar(range(1, 31), by_date)


# In[18]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[19]:


bar(range(1, 31), by_date_sorted)
xticks(range(1,31), by_date_sorted.index)
xlabel('Date of the month')
ylabel('Frequency')
title('Frequency by DoM - uber - Apr 2014')


# ## Analysis of the hour

# In[24]:


hist(data.hour, bins=24, range=(.5, 24), rwidth=.8, color='#FF0000')


# ## Analysis of the Weekday

# In[26]:


hist(data.weekday, bins=7, range =(-.5,6.5), rwidth=.8, color='#AA6666')
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())


# ## Color Analysis (hour,dow)

# In[29]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()
seaborn.heatmap(by_cross)


# ## Lat and Lon

# In[32]:


hist(data['Lat'], bins=100, range = (40.5, 41), color='#FF6347');


# In[33]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9), color='#FF6347');


# In[34]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9), color='g', alpha=.5, label = 'longitude')
grid()
legend(loc='upper left')
twiny()
hist(data['Lat'], bins=100, range = (40.5, 41), color='r', alpha=.5, label = 'latitude')
legend(loc='best')
("")


# In[35]:


figure(figsize=(20, 20))
plot(data['Lon'], data['Lat'], '.', ms=1, alpha=.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)


# In[ ]:




