# %%
#Importing required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
#Read the dataset
df = pd.read_csv('Sales_Analysis.csv',delimiter=',')

# %%
#Print top 20 rows
df.head(20)

# %%
# Q1 - Gráfico de Vendas por produto
# Convertendo as colunas 'Quantity Ordered' e 'Price Each' para o tipo numérico
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
df['Price Each'] = pd.to_numeric(df['Price Each'], errors='coerce')

# Agrupando os dados pelo nome do produto e somando a quantidade vendida
sales_by_product = df.groupby('Product')['Quantity Ordered'].sum()

# Criando o gráfico circular
plt.figure(figsize=(10, 8))
sales_by_product.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Vendas por Produto')
plt.ylabel('')
plt.show()

# %%
# Agrupando os dados pela cidade e contando o número de clientes
customers_by_city = df['City']

# Exibindo a cidade com mais clientes
print(customers_by_city.idxmax(), customers_by_city.max())

# %%



