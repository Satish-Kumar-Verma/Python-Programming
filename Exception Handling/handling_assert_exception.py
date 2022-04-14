

try:
    num = int(input("Enter a number between 5 and 10 : "))
    assert num >= 5 and num <= 10
    print(f"Num : {num}")

except AssertionError as e:
    print("The condition is not fulfilled!")


# num = int(input(""))
# assert num >= 5 and num <= 10
# print("Hi")