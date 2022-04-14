

def fibo():
    first_num, second_num = 0, 1
    yield first_num
    while True:
        first_num, second_num = second_num, first_num + second_num
        # temp = second_num
        # second_num = first_num + second_num
        # first_num = temp
        yield first_num


def square(nums):
    for num in nums:
        yield num ** 2


fibo_ = fibo()
sq = square(fibo_)

for i in range(10):
    print(next(sq))


# fibo_num = fibo()
# for i in range(100):
#     print(next(fibo_num))
