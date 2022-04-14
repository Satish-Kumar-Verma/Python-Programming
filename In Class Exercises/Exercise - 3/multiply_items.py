
my_list = list(map(int, input("Enter a list : ").split()))

result = 1

for item in my_list:
    result *= item
# for i in range(len(my_list)):
#     result *= my_list[i]

print(result)