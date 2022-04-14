
items = list(map(int, input("Enter a list : ").split()))

result = 0

for item in items:
    result += item


items.sort()
print(f"Minimum : {items[0]}")

print(result)
