import time

def square_gen():
    num = 1
    while True:
        yield num ** 2
        num += 1

start = time.time()
sq = square_gen()
for i in range(2000000):
    print(next(sq))

stop = time.time()
print(stop - start)
