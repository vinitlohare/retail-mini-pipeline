import pandas as pd
import random

rows = 1000

data = {
    "order_id": list(range(1, rows+1)),
    
    "customer_name": [
        random.choice(["Amit", "Rahul", "Neha", "Pooja", None]) 
        for _ in range(rows)
    ],
    
    "age": [
        random.choice([22, 25, 30, 35, None]) 
        for _ in range(rows)
    ],
    
    "product": [
        random.choice(["Laptop", "Mobile", "Tablet", "Headphones", None]) 
        for _ in range(rows)
    ],
    
    "quantity": [
        random.choice([1, 2, 3, None]) 
        for _ in range(rows)
    ],
    
    "price": [
        random.choice([10000, 15000, 20000, None]) 
        for _ in range(rows)
    ]
}

df = pd.DataFrame(data)

# Add duplicates (real-world issue)
df = pd.concat([df, df.sample(50)])

# Shuffle data
df = df.sample(frac=1).reset_index(drop=True)

# Save file
df.to_csv("data/raw_retail_data.csv", index=False)

print("Messy retail data generated!")