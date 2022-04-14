#
# try:
#     pass  # this will execute first
#
# except:  # this will execute only if it catches an error
#     pass
#
# else:  # this will not execute if the except block does
#     pass
#
# finally:  # this will always execute (no matter what)
#     pass


a = input("A : ")
b = input("B : ")

try:
    c = a / b
    print(c)

except Exception as error:
    print(error)

else:
    print("Printing from else block!")

finally:
    print("Printing from finally block!")

