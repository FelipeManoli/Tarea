#!/usr/bin/env python
# coding: utf-8

# # Ejercicios con `pandas`

# Importe las librerías necesarias:

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# Imprima las versiones de todas la librerías

# In[3]:


pandas._version


# Importe los datos desde [aqui](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). Asígnelos a una variable `chipo`.

# In[6]:


chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", sep="\t")


# Muestre las primeras 10 entradas del dataframe

# In[12]:


chipo.head(10)


# Cual es el número total de observaciones en el dataset?

# In[21]:


len(chipo)
# solucion 1


# In[1]:



# solucion 2


# Cuantas columnas hay en el dataset? Copielas a una lista.

# In[31]:


a=list(chipo.columns)
len(a)


# Imprima el nombre de las columnas

# In[30]:


print(a)


# Como está indexado el dataset?

# In[32]:


chipo.index


# Cual fue el objeto más pedido?

# In[45]:


chipo.item_name.value_counts()
#Chicken Bowl


# Para el objeto más pedido, cuantos fueron?

# In[ ]:


Chicken Bowl


# Cual fue el item más pedido en la columna `choice_description`?

# In[47]:


chipo.choice_description.value_counts()


# Cuantos items fueron pedidos en total?

# In[51]:





# Convierte el precio en un `float`

# In[ ]:





# Cuanto fue la ganancia total en el periodo del dataset?

# In[ ]:





# Cúantos pedidos se hicieron?

# In[ ]:





# Cual fue el promedio de ganancia por orden?

# In[ ]:





# Cuántos items se vendieron en total?

# In[ ]:




