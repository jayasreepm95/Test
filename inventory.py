stock = [15, 3, 0, 22, 8, 1]

for i in stock:

# 1. Check if stock is 0
    if i == 0:
        print(i, " Out of Stock")

# 2. Check if stock is between 1 and 5
    elif i >= 1 and i <= 5:
        print(i, "Restock Immediately")

# 3. Ignore all other values
    else:
        pass