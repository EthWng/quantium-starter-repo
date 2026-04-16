import pandas as pd # imports and gives name

df = pd.concat([ # .concat combines tables together
    pd.read_csv("data/daily_sales_data_0.csv"), # reads csv and turns into table
    pd.read_csv("data/daily_sales_data_1.csv"),
    pd.read_csv("data/daily_sales_data_2.csv"),
])

# gets product column 
# checks if value == "pink morsel"
# keeps only those rows
df = df[df["product"] == "pink morsel"] 


df["price"] = df["price"].str.replace("$", "").astype(float) # replaces $ with nothing and casts to float
df["sales"] = df["price"] * df["quantity"] # creates new column = sales column * quantity column
df = df.drop(columns=["product", "price", "quantity"]) # drops columns
df = df.iloc[:, [2, 1, 0]] # reorders columns (: - keep all rows)
df.to_csv('task.csv', index=False) # creates file without the index