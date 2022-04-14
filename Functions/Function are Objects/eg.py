# It is possible to assign a function to a variable
# def my_fun():
#     print("Hello")
#
# a = my_fun()
#
# print(a)

# It is possible to define one function in another function

# def my_fun():
#     a = 4
#     def hello(a):
#         print("A = ", a)
#     return hello(a)
#
# a = my_fun()
# print(a)

# It is also possible to pass a function as a parameter to another function # Eg: map(int, input().split())
# It is also possible that a function can return another function
def my_fun():
    print("Hello")

def my_another_fun(fun):

    # fun()
    return fun()

my_another_fun(my_fun)

