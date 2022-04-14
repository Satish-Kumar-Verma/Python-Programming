# No. 1
# i = 1

# while i < 11:
#     print(i)
#     i += 1

# No.2
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# No.17

# series = 0
# result = 0
# n = int(input("Enter the value of n : "))

# for i in range(n):
#     series = (series * 10) + 2
#     result += series

# print(f"Sum of the series till n is : {result}")

# No.18

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(4, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# No.5

# list_input = list(map(int, input("Enter a list : ").split()))

# for item in list_input:
#     if item % 5 == 0 and item <= 150:
#         print(item)
    
#     elif item > 500:
#         break

# No.10

# for i in range(5):
#     print(i)
#     if i >= 3:
#         break

# else:
#     print("Done!") 


# No.11

# start, end = tuple(map(int, input("Enter the range : ").split()))


# for i in range(start, end + 1):
#     if i == 2:
#         print(i)
    
#     elif start < 2 and end < 2:
#         print("There is no prime number in the given range")
    
#     else:
#         counter = 0
#         for j in range(2, int(i/2) + 1):
#             if i % j == 0:
#                 counter += 1
#                 break
            
#         if counter < 1:
#             print(i)
    
# No. 12

# first_term = 0
# second_term = 1
# print(first_term, end=" ")
# print(second_term, end=" ") # Ctrl + D

# for i in range(8):
#     third_term = first_term + second_term
#     first_term = second_term
#     second_term = third_term
#     print(third_term, end=" ")
# print()

# No.13

# fact = 1
# for i in range(1, 6):
#     fact *= i
# print(fact)


# No. 14

# n = int(input("N : "))
# num = 0
# while n > 0:
#     num = (num * 10) + (n % 10)
#     n = int(n / 10)

# print(num)

# Homework

# tp = (1, 2, 3, 4, 5, 6, 7, 8)
# print(f"You can slice between 1 and {len(tp)}.")
# start = int(input("Enter the start position : "))
# end = int(input("Enter the end position : "))

# print(tp[start:end])


tp_input = tuple(map(int, input("Enter the tuple : ").split()))

print(f"You can do slicing from index 0 to {len(tp_input) - 1}.")

while True:
    start, stop = tuple(map(int, input("Start:Stop : ").split(":")))
    if stop < len(tp_input):
        break

for i in range(start, stop):
    print(tp_input[i], end=" ")

print()



