

# class Sum:
#     def __init__(self, a, b):
#         print(a + b)
# Sum(3, 7)
# Sum(2.1, 7)
# Sum(7, 2.1)

class Sum:
    def __init__(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print(a + b + c)

        elif a is not None and b is not None:
            print(a + b)

        elif a is not None and c is not None:
            print(a + c)

        elif b is not None and c is not None:
            print(b + c)

        else:
            print("Please enter at least two arguments.")


s = Sum(1, 2, 3)
s1 = Sum(1, 3)
s2 = Sum(None, 2, 6)
s3 = Sum(7, None, 5)
s4 = Sum()
