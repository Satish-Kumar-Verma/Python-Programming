
input_list = []

tp_count = int(input("How many tuples do you want in the list : "))

for i in range(tp_count):
    tp = tuple(map(int, input("Enter a tuple [integers only] : ").split()))
    input_list.append(tp)

print(input_list)
temp_list = input_list.copy()
result = []



for j in range(len(input_list)):
    min = temp_list[0]
    for i in range(len(temp_list)):
        if temp_list[i][-1] < min[-1]:
            min = temp_list[i]
    temp_list.remove(min)
    result.append(min)

result.reverse()

print(result)

# result = sorted(input_list, key=lambda n:n[-1])
# input_list.sort(key=lambda n:n[-1], reverse=True)
# print(input_list)
