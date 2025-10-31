import numpy as np
import matplotlib
import pandas as pd

import matplotlib.pyplot as plt
matplotlib.use('Agg')

# 1️⃣ Create a sample dataset using pandas
data = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grapes"],
    "Price": [120, 40, 60, 100, 80]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2️⃣ Use NumPy to increase all prices by 10%
df["updated_Price"] = np.array(df["Price"]) * 1.10
print("After 10% price increase:")
print(df)
print("\n")

# 3️⃣ Plot a bar chart comparing old vs new prices
plt.figure(figsize=(7, 4))
plt.bar(df["Product"], df["Price"], label="Original Price", alpha=0.6)
plt.bar(df["Product"], df["Updated_Price"], label="Updated Price", alpha=0.6)
plt.title("Product Price Comparison")
plt.xlabel("Product")
plt.ylabel("Price (₹)")
plt.legend()

plt.savefig("price_comparison.png")

