from collections import Counter

# Read number of pairs and their sizes
N = int(input())
pairs = list(map(int, input().split()))
pairs_list = Counter(pairs)

# Read number of customers
m = int(input())
total_price = 0

# Process each customer's request
for _ in range(m):
    size_str, price_str = input().split()
    size = int(size_str)
    price = int(price_str)

    # Check if the requested size is in stock
    if pairs_list[size] > 0:
        total_price += price
        pairs_list[size] -= 1  # Decrease available stock

print(total_price)
