#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Analysis Using Python
# Python and its following libraries are used to analyze Zomato data.

Numpy– With Numpy arrays, complex computations are executed quickly, and large calculations are handled efficiently.
Matplotlib– It has a wide range of features for creating high-quality plots, charts, histograms, scatter plots, and more.
Pandas– The library simplifies the loading of data frames into 2D arrays and provides functions for performing multiple analysis tasks in a single operation.
Seaborn– It offers a high-level interface for creating visually appealing and informative statistical graphics. 
# To address our analysis, we need to respond to the subsequent inquiries:
# 
# Do a greater number of restaurants provide online delivery as opposed to offline services?
# Which types of restaurants are the most favored by the general public?
# What price range is preferred by couples for their dinner at restaurants?
# Before commencing the data analysis, the following steps are followed.
# 
# Following steps are followed before starting to analyze the data.

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# In[4]:


dataframe = pd.read_csv("C:\\Users\\Asus\\OneDrive\\Desktop\\Zomato data .csv")
print(dataframe.head())


# In[20]:


import pandas as pd

def handlerRate(value):
    valuestr = str(value).split('/')
    return float(valuestr[0])

# Create a sample DataFrame (replace with your actual data)
data = {'rate': ['1/2', '3/4', '5/6']}
dataframe = pd.DataFrame(data)

dataframe['rate'] = dataframe['rate'].apply(handlerRate)
print(dataframe)



# In[21]:


dataframe.info()


# We will now examine the data frame for the presence of any null values. This stage scans each column to see whether there are any missing values or empty cells. This allows us to detect any potential data gaps that must be addressed.
# 
# 

# In[7]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")


# In[8]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)


# In[9]:


max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']

print("Restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)


# In[27]:


sns.countplot(x=['online_order'])





# In[14]:


plt.hist(dataframe['rate'],bins=5)
plt.title("Ratings Distribution")
plt.show()


# In[15]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# In[16]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)


# In[17]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()

# CONCLUSION: Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders. This suggests that clients prefer to place orders in person at restaurants, but prefer online ordering at cafes.# 
# In[ ]:




