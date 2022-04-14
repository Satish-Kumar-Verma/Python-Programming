#
# stop_now = False
# n = None
# sum = 0
# while not stop_now:
#     n = int(input("Enter a positive integer : "))
#     if (n >= 0):
#         sum += n
#
#     else:
#         stop_now = True
# print(n)
# print("Sum =", sum)


sum = 0

while True:
    n = int(input("Enter a positive integer : "))
    if (n >= 0):
        sum += n

    else:
        break

print(sum)