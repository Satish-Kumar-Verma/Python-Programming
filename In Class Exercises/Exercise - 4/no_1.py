lot = []

for i in range(5):
    temp_tp = tuple(map(int, input("Enter a tuple : ").split()))
    lot.append(temp_tp)

print(lot)
temp_lot = lot[:]

result = []

for i in range(0, len(lot)):
    temp_v = lot[i][-1]
    for j in range(1, len(temp_lot)):
        if temp_v <= temp_lot[j][-1]:
            result.append(lot[i])
            temp_lot.remove(lot[i])
        
        else:
            temp_v = lot[j][-1]

result = result[::-1]
result.append(temp_lot[0])
# result = sorted(lot, key=lambda n:n[-1])
# def last(n):
#     return n[-1]
# lot.sort(key=last)
print(result)