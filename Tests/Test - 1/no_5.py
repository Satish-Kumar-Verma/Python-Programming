input_num = int(input("Enter an integer : "))

reverse_num = 0

while(input_num > 0):
    reverse_num = (reverse_num * 10) + input_num % 10
    input_num //= 10

print(reverse_num)

