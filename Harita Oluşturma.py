#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#İstanbul'da ki mesaj panolarının yoğunluğunun göterildiği verileri okuma işlemi

df = pd.read_excel (r'C:/Users/elifn/OneDrive/Masaüstü/yogunluk.xlsx')


# In[3]:


df


# In[4]:


df.info()


# In[5]:


#ROTA ID'lerin ilçelerini gösteren kordinat tablosu

koordinat = pd.read_excel (r'C:/Users/elifn/OneDrive/Masaüstü/koordinat.xlsx')


# In[6]:


koordinat


# In[7]:


#yoğunluk tablosu ile bulundukları ilçelerin gösterildği kordinat tablosunun birleştirilmesi

birlesim=pd.merge(df,koordinat,on='Rota ID',how='inner')
birlesim


# In[8]:


s=birlesim.groupby(['Rota ID','Durum'])
s=s.count()
s


# In[9]:


sonuc =  pd.DataFrame(columns=('Rota ID', 'Rota İsim', 'Açık', 'Akıcı', 'Yoğun', 'Enlem', 'Boylam'))
for i in range(1,100):
    
    a=(birlesim[birlesim["Rota ID"]==i]["Durum"].value_counts())
    
    sonuc = sonuc.append([{'Rota ID':i, 
                           'Rota İsim':((birlesim[birlesim["Rota ID"]==i]["Rota İsmi"]).head(1)).iloc[0],
                            'Açık':float(a["AÇIK"]),
                            'Akıcı':float(a["AKICI"]),
                            'Yoğun':float(a["YOĞUN"]),
                            'Enlem':((birlesim[birlesim["Rota ID"]==i]["Enlem"]).head(1)).iloc[0],
                            'Boylam':((birlesim[birlesim["Rota ID"]==i]["Boylam"]).head(1)).iloc[0]}],
                         ignore_index=True)

sonuc


# In[10]:


#harita çizimi için kullancağımız kütüphane
import folium


# In[11]:


help(folium.Icon)


# In[12]:


m = folium.Map(location=[41.013611,28.955], control_scale=True, zoom_start=11,attr = "text some")
df_copy = sonuc.copy()

# 99 bölgeyi haritada göstermek için açılan döngü
for i in range(0,99):
    
    
    if df_copy.iloc[i]['Açık']>df_copy.iloc[i]['Yoğun']+df_copy.iloc[i]['Akıcı']:
        # popup ekranında yazılacak yazı 
        html="""
        <h4> ADRES: </h4>""" + str( df_copy.iloc[i]['Rota İsim'])+"""<h4> DURUM: </h4> Açık"""
        iframe = folium.IFrame(html=html, width=150, height=200)
        popup = folium.Popup(iframe)
        folium.Marker(
        location=[df_copy.iloc[i]['Enlem'], df_copy.iloc[i]['Boylam']],
        popup=popup,
        tooltip=str(df_copy.iloc[i]['Rota İsim']),
        icon=folium.Icon(color='blue',icon='calendar',prefix="fa"),
        ).add_to(m)
        
    else:
        # popup ekranında yazılacak yazı 
        html="""
        <h4> ADRES: </h4>""" + str( df_copy.iloc[i]['Rota İsim'])+"""<h4> DURUM: </h4> Akıcı ve Yoğun"""
        iframe = folium.IFrame(html=html, width=150, height=200)
        popup = folium.Popup(iframe)
        folium.Marker(
        location=[df_copy.iloc[i]['Enlem'], df_copy.iloc[i]['Boylam']],
        popup=popup,
        tooltip=str(df_copy.iloc[i]['Rota İsim']),
        icon=folium.Icon(color='red',icon='calendar',prefix="fa"),
        ).add_to(m)
        
#ekrana haritayı getirme 
m


# In[ ]:





# In[ ]:




