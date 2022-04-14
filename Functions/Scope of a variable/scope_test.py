


# total = 0
#
# def sum(a, b):
#     global total
#     total = a + b
#     print(f"Total inside the function : {total}")
#
# sum(2, 5)
# print(f"Total Outside the function : {total}")


# Can we use both local and global variables at the same time with the same name?

# a = 1
#
# def my_fun():
#     global a
#     a = 5
#     print("a =", a)
#
# my_fun()
# print("a :", a)


# The solution!

a = 1
b = 7

def my_fun():
    a = 2
    x = globals()['a']
    print(f"Global a = {x}, Local a = {a}")

my_fun()
print(a)

