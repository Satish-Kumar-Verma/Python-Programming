no_of_rotation = int(input("Enter the value of n : "))

input_list = input("Enter a list : ").split()

for i in range(no_of_rotation):
    input_list = input_list[-1:] + input_list[:-1]

print(input_list)