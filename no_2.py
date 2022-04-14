input_str = input("Enter a string  : ")

if input_str.__eq__(input_str[::-1]):
    print("It is a palindrome.")

else:
    print("It is not a palindrome.")