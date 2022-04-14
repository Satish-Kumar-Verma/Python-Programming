
# my_set = {10, 20, 30, 40, 50, 60, 30}
#
# print(my_set)


# Creating a set using set() Constructor.

# my_set = set("Hello")
# print(my_set)

# my_list = [1, 2, 3, 4, 5]
# my_set = set(my_list)
# print(my_set)

# Can we retrieve the elements using slicing
# or indexing?

# my_set = {10, 20, 30, 40, 50}
# print(my_set[2:])
# print(my_set[0])


# How can we add elements to a set?
#
# my_set.update([60])
# print(my_set)

# How can we remove an element from a set?

# my_set.remove(30)
# print(my_set)

# How to print a set using for-loop?

# li = [1, 2, 3, 4, 5]
# for i in range(len(li)):
#     print(li[i])

# for item in li:
#     print(item)

# for item in my_set:
#     print(item)


# Frozen set

# fs = frozenset(my_set)
# print(fs)


# NO.1

# input_ = set(map(int, input("Enter a set : ").split()))
# print(input_)

# li = list(input_)
# print(li)

# No. 2

# my_set = {10, 20, 30, 40, 50}
#
# for item in my_set:
#     print(item)

# No.3
# my_set = {10}
# my_set.update([20, 30])
# my_set.add(100)
# print(my_set)


# No. 4

# my_set = {10, 20, 30, 40, 50}
# my_set.remove(10)
#
# print(my_set)

# NO. 5

# my_set = {10, 20, 30, 40, 50}
# n = 10
# if n in my_set:
#     my_set.remove(n)
#     print(my_set)
#
# else:
#     print("Not hi")

# No. 6 Intersect

# set1 = {"green", "blue"}
# set2 = {"blue", "yellow"}
# set3 = set1 & set2
# print(set3)

# No. 7 Union

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7, 8}
#
# setn = set1.union(set2)
# print(setn)


# No.8 Set difference

# setx = {"mango", "orange"}
# sety = {"mango", "apple"}
#
# setn = sety.difference(setx)
# print(setn)

# No. 9 Symmetric difference

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# setn = set1.symmetric_difference(set2)
# print(setn)

# No. 10 Checking subset

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3, 4, 5, 6, 7}
#
# if set1.issubset(set2):
#     print("Yes")
#
# else:
#     print("No")



# No.11 shallow copy
#use copy()

# No. 12 remove all the elements from a set
#
# set1 = {1, 2, 3, 4, 5}
# set1.clear()
# print(set1)

# No. 13 Creating a frozenset

# set1 = {1, 2, 3, 4, 5}
# fs = frozenset(set1)
# print(fs)

# No.14 Finding max and min in a set
#
# set1 = {1, 2, 3, 4, 5, 6}
# print(f"Max = {max(set1)}")
# print(f"Min = {min(set1)}")

# No.15 Finding the length of a set

# set1 = {1, 2, 3, 4, 5}
# print(len(set1))

# No.16 checking if a value is present in the set

# set1 = {1, 2, 3, 4, 5}
# if 2 in set1:
#     print("Hi")


# No. 17 Checking if two given sets have no elements in common

# set1 = {2, 3, 4, 5, 7}
# set2 = {1, 8, 9}
# if len(set1 & set2) > 0:
#     print("They have!")
#
# else:
#     print("They don't have!")


# No.18 Checking superset

# seta = {1, 2, 3, 4, 5}
# setb = {1, 2, 3, 4, 5, 6}
#
# if seta.issuperset(setb):
#     print("Yes!")
#
# else:
#     print("NO!")

# No.19 finding elements which are not in the another set

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 3, 4, 7, 8}
#
# print(set1.difference(set2))

# No. 20 remove the intersection of a 2nd set from the 1st set.

# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 4, 6, 8}

# symmetric = set1 & set2
#
# result = set1.difference(symmetric)
# print(result)

# result = set1.difference(set1 & set2)
# print(result)

