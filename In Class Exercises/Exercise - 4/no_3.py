
tp = tuple(input("Enter a tuple : ").split())

print(tp)

temp_list = list(tp)
print(temp_list)

for item in tp:
    if temp_list.count(item) > 1:
        temp_list.remove(item)

tp = tuple(temp_list)
print(tp)