
# stop = False
# i = 1
# while True:
#     while True:
#         i = 2
#         print(f'Printing i in the innermost loop {i}')
#         if i == 2:
#             break
#
#     print(f"Printing i in the outermost loop {i}")
#     if i == 2:
#         break
# print("Hello!")
# a = b = 5
# print(f"{a}\t{b}")

# a = 5
# k = 1
# for i in range(1, 6):
#     for j in range(1, a - 3):
#         print(f"{i} x {k} = {i * k}\t", end="")
# a = 4
# print(a, end="")
# print(a, end="")

a = 4
for i in range(1, 11):
    for j in range(1, a + 1):
        print(f"{j} x {i} = {j * i}\t", end="")
    print()
