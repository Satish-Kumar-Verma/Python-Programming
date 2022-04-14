
def sq_fun(x):
    """This function returns the square of any number!""" #doc-strings
    # y = x * x
    # y = x ** 2
    # return y
    return x ** 2



def main():
    num = int(input("Enter any number : "))
    print(f"Square of {num} is {sq_fun(num)}.")
    print(f"Square of {num + 1} is {sq_fun(num + 1)}.")
    print(sq_fun.__doc__)

if __name__ == "__main__":
    main()