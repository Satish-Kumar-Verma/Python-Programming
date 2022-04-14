# Testing on integers (Immutable data type)

# a = 12
# # b = a
# b = 12
# print(id(a))
# print(a)
# print(b)
# print(id(b))

# integers with function

# def sum(a, b):
#     print(f"ID of a inside functon {id(a)}")
#     b = 4
#     print(f"ID of b inside functon {id(b)}")
#     print(a + b)
#
# b = 3
# a = 4
# sum(a, b)
# print(f"ID = {id(a)}")
# print(f"ID = {id(b)}")

# Testing it with list [Mutable data type]

# def my_fun(l):
#     l[0] = 5
#     l[1] = 8
#     l.append(4)
#     print("list : ", end="")
#     for item in l:
#         print(item, end=" ")
#     print()
#
#     print("Id(l) =", id(l))
#
# li = [1, 2, 3, 4, 5, 6]
# print("ID(li) =", id(li))
# my_fun(li)




