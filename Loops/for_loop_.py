
a = 13

# for i in range(20, 15, -1): # i = 20, 19, 18, 17, 16
#     print(a)
# range(start, stop, incre...)

# for i in range(1, 11, 1): #start = 1, stop = 10, incre.. = 1
#     print(i)

for i in range(1, 11, 1):  # 2 x 1, 2 x 2, 2 x 3 , start = 1, end = 11, incre.. = 1
    # print(f"{a} x {i} = {a * i}")
    # print(str(a) + " x " + str(i) + " = " + str(a * i))
    print("{} x {} = {}".format(a, i, a * i))
