

def test():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


t = test()

#
# for item in t:
#     print(item)

length = 0
try:
    for i in range(4):
        print(next(t))
        length += 1

except StopIteration as e:
    pass

print(length)
