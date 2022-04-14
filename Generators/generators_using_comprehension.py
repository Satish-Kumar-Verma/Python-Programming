

mylist = [1, 2, 3, 4, 5]
# my_tp = (1, 2, 3)

# mylist = [i ** 2 for i in mylist]
# print(mylist)

my_gen = (i ** 2 for i in mylist)
# my_tple = tuple(i ** 2 for i in my_tp)
# print(my_gen)
# print(my_tple)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
