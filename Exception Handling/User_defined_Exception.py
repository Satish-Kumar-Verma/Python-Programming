# User-Defined exception

class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


def check_list(lst):
    for item in lst:
        if item < 5:
            raise MyException("Please provide numbers greater than or equal to 5")


try:
    check_list([1, 2, 3, 4, 5])

except MyException as me:
    print(me)
