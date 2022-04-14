

def my_gen(num):
    n = num + 1

    print("This will be printed first!")
    yield n

    n = n + 1
    print("This will be printed second!")
    yield n

    n = n + 1
    print("This will be printed at last!")
    yield n


x = my_gen(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
