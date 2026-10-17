import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 


df=pd.read_csv('data.csv') 
print(df.head()) #return start 5 rows of the dataset
print(df.columns.to_list()) #return all column names
print(df.info())    #check the data types of each column and the number of non-null values

#Data Cleaning 
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_') 
print(df.columns.to_list()) 
df=df.drop_duplicates() 

#Numeric columns cleaning
df['price']=df['price'].astype(str).str.replace(',', '').astype(float) 
print(df['price'])  
df['area']=df['area'].astype(str).str.replace(',', '').astype(int)
print(df['area'])  
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(',', '').astype(int)
print(df['rate_per_sqft']) 

#Categorical columns cleaning
df['status']=df['status'].str.strip().str.lower()
print(df['status']) 
df['rera_approval']=df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type']=df['flat_type'].str.strip().str.lower()
print(df['rera_approval'])
print(df['flat_type']) 

df=df.drop_duplicates()  
print(df.info())  

#Now Its a time to ans the questions 

#1 Which is the costliest flat in the dataset?  
costlist_flat=df.loc[df['price'].idxmax()] # return a row of the costliest flat in the dataset
print(costlist_flat)
costly=df['price'].max() # return the costliest flat price in the dataset
print(costly) 

#2 Which locality has the highest average price? 
higest_avg_price=df.groupby('locality')['price'].mean().idxmax() # return the locality with the highest average price
print(higest_avg_price)

print(df.groupby('locality')['price'].mean().sort_values(ascending=False).head(20)) # return the average price of each locality in descending order

#3 Which locality has the highest rate per square foot? 
higeht_rate_per_sqft=df.groupby('locality')['rate_per_sqft'].mean().idxmax() # return the locality with the highest rate per square foot
print(higeht_rate_per_sqft)  

# 4 Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price=df[df['status']=='ready to move']['price'].mean() # return the average price of ready-to-move properties
under_constaruction_avg_price=df[df['status']=='under construction']['price'].mean() # return the average price of under-construction properties
if ready_to_move_avg_price>under_constaruction_avg_price:
    print("Yes, ready-to-move properties cost more than under-construction properties.")
else:
    print("No, under-construction properties cost more than ready-to-move properties.") 


# 5 Do RERA-approved properties command a price premium?     
rera_approved_avg_price=df[df['rera_approval']==True]['price'].mean() # return the average price of RERA-approved properties        
not_rera_approved_avg_price=df[df['rera_approval']==False]['price'].mean() # return the average price of non-RERA-approved properties   
if rera_approved_avg_price > not_rera_approved_avg_price:
    print("Yes, RERA-approved properties command a price premium.")     
else:
    print("No, non-RERA-approved properties command a price premium.")


# 6 How does area (sqft) impact property price?        
# sns.scatterplot(x='area', y='price', data=df)
# plt.title('Area vs Price')
#plt.show() 

#7 Which BHK configuration is the most expensive on average?
most_expensive_bhk=df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax() # return the BHK configuration with the highest average price
print(most_expensive_bhk)

#8 Which property type (Apartment, Floor, Plot) is the costliest?   
most_expensive_property_type=df.groupby('flat_type')['rate_per_sqft'].mean().idxmax() # return the property type with the highest average price
print(most_expensive_property_type)

#9 Do certain builders or companies consistently price higher top 5 ?   
top_5_builders=df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5) # return the top 5 builders with the highest average price
print(top_5_builders)

#10 Are larger homes always more expensive per square foot? 
larger_homes_expensive=df.groupby('area')['rate_per_sqft'].mean().sort_values(ascending=False).head(5) # return the larger homes with the highest average price per square foot
print(larger_homes_expensive)  

sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.title('Area vs Rate per Sqft')  
plt.show()