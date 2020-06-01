#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys


# In[2]:


sys.version


# In[3]:


df = pd.read_excel(r'C:\Users\Pc\Downloads\Yogunluk.xlsx')


# In[4]:


df


# In[5]:


print(df.info())


# In[6]:


df.replace({'AÇIK': '0'},inplace=True)
df.replace({'AKICI': '1'},inplace=True)
df.replace({'YOĞUN': '2'},inplace=True)


# In[7]:


df


# In[8]:


grouped=df.groupby(['Rota ID','Durum']).count()[['Başlangıç Tarihi']]
grouped


# In[9]:


grouped[:30].plot.bar()


# In[10]:


grouped1=df.groupby(['Rota ID'])[['Rota ID']].count()
grouped1.head(10)


# In[11]:


grouped1[:10].plot.bar()


# In[12]:


grouped2=df.groupby(['Durum'])[['Rota ID']].count()
grouped2


# In[13]:


sns.catplot(x="Durum", kind="count", palette="ch:.25", data=df)
#Açık, Akıcı ve Yoğun durumunda olan panoların sayısı


# In[14]:


grouped3=df.groupby(['Rota ID'])[['Durum']]
grouped3.head()


# In[15]:


sns.catplot('Rota ID',data=df[:50000],hue='Durum',kind='count',height=10, aspect=2)
sns.set_palette("husl",4)
plt.title("DEĞİŞKEN MESAJ PANOLARINDA GÖSTERİLEN YOĞUNLUK VERİSİ")


# In[16]:


grouped3 = df.groupby(['Başlangıç Tarihi'])[['Rota ID']].count()
grouped3.head(10)


# In[17]:


sns.set_palette("RdBu", n_colors=3)
grouped3[:10].plot.barh()


# In[18]:


sns.set_palette("RdBu", n_colors=7)
df.groupby('Başlangıç Tarihi')['Rota ID'].nunique().plot(kind='bar')
plt.show()


# In[19]:


sns.set_palette("ch:2.5,-.1,dark=-.7")
df['Rota ID'].plot(kind='hist',bins=[0,100,200,300,400,500],rwidth=0.8)
plt.show()

