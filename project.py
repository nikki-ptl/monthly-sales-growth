#Data load

import pandas as pd


df = pd.read_excel("sales_raw_500.xlsx")
print(df)


# Remove Duplicates

df = df.drop_duplicates()
print(df)


#Fix Order_Date


df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors ='coerce')
print(df)


#Drop blank row in Order Date

df = df.dropna(subset=['Order_Date'])
print(df)


#Add column 

df['Profit'] = df['Sales']-df['Cost']
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month

print(df)


#save file in csv

df.to_csv("sales_cleaned.csv",index=False)


# Python + Excel + SQL

import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv("sales_cleaned.csv")
print(df)

engine = create_engine('mysql+pymysql://root:Nikita%40321123@localhost:3306/salesdb')

df.to_sql(name='sales_data',con=engine,if_exists='replace',index=False)
print(df)





#Add data cleaning and database connection code

