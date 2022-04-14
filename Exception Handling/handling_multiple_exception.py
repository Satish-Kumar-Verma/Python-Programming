

def avg(lst):
    tot = 0
    for item in lst:
        tot += item

    avg = tot / len(lst)

    return avg, tot


try:
    avg, tot = avg([1, 2, 3, 4, 5, "a"])
    print(f"Average : {avg}, Total : {tot}")

# except TypeError as e:
#     print("Type error. please provide numbers only ...")
#
# except ZeroDivisionError as e:
#     print("Please don't give empty list you gay!")
except (ZeroDivisionError, TypeError) as e:
    print(e)

finally:
    print("Bye Bye!")
