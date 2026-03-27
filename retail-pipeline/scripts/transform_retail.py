import pandas as pd  

df= pd.read_csv("data/raw_retail_data.csv")
print("before cleaning")
# isnull->check the null values and .sum() → counts missing values per column
print(df.isnull().sum()) 

df["customer_name"] = df["customer_name"].fillna("Unknown")

df["product"]  = df["product"].fillna("unknown")

df["age"]= df["age"].fillna(df["age"].mean())

df["quantity"] = df["quantity"].fillna(1)

df["price"]= df["price"].fillna(0)

print("\nAfter Cleaning")
print(df.isnull().sum())

df.to_csv("data/cleaned_retail_data.csv",index=False)

print("Cleaned completed")

df["total_amount"]= df["quantity"] *df["price"]

print("\nAfter Adding total column")
print(df[["quantity","price","total_amount"]].head())
