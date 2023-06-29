#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
df = pd.read_csv('raw.githubusercontent.com_KeithGalli_pandas_master_pokemon_data.csv')


print(df.tail(3))


# In[9]:


print(df.tail(100))


# In[10]:


df.sort_values(['Type 1', 'HP'], ascending=[1,0])

df



# In[11]:


df.describe()


# In[12]:


# Making Changes to the DATA :)

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

df.head(5)


# In[13]:


#Saving our data :)
# df.to_csv('modified.csv', index=False)

#df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')


# In[24]:


#Filtering Data 

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

new_df.reset_index(drop=True, inplace=True)

new_df

new_df.to_csv('filtered.csv')


# In[16]:


#conditional changes :)
# df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']

# df

df = pd.read_csv('raw.githubusercontent.com_KeithGalli_pandas_master_pokemon_data.csv')


df

#hmmm. not working? nvm it worked. 


# In[17]:


df['count'] = 1

df.groupby(['Type 1', 'Type 2']).count()['count']


# In[27]:


#Aggregate Statistics 

df = pd.read_csv('raw.githubusercontent.com_KeithGalli_pandas_master_pokemon_data.csv')

df.groupby (['Type 1']).mean().sort_values ('Defense', ascending=False)


# In[28]:


df.groupby (['Type 1']).mean().sort_values ('Attack', ascending=False)


# In[29]:


df.groupby (['Type 1']).mean().sort_values ('HP', ascending=False)


# In[34]:


df.groupby (['Type 1']).count()

df['count'] = 1

df


# In[35]:


df.groupby (['Type 1', 'Type 2']).count()['count']


# In[ ]:




