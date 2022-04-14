input_list = []

tp_count = int(input("How many tuples do you want in the list : "))

for i in range(tp_count):
    tp = tuple(map(int, input("Enter a tuple [integers only] : ").split()))
    input_list.append(tp)

print(input_list)

for i in range(len(input_list)):
    for j in range(i + 1, len(input_list)):
        if input_list[i][-1] > input_list[j][-1]:
            input_list[i], input_list[j] = input_list[j], input_list[i]

print(input_list)

input_list.reverse()
print(input_list)
        