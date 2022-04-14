
l_o_s = input("Enter strings seperated by a space : ").split()

counter = 0

for item in l_o_s:
    if len(item) >= 2 and item[0] == item[-1]:
        counter += 1

print(f"Count : {counter}")