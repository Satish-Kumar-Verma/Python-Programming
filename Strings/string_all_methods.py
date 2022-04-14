#
# test_string = "Banana"
#
# for i in test_string:
#     print(i, end="")
#
# print()
# print(f"The length of the string is : {len(test_string)}")

#in / not in

# test_string = "Hello, I am fine."
#
# if "I" in test_string:
#     print("Found!")
#
# if "Hmmm" not in test_string:
#     print("Not found!")

#String slicing

# test_string = "Hello, World!"
# a = test_string[2:]
# a = test_string[2:5]
# a = test_string[:5]
# a = test_string[-5:-2]
# a = test_string[-2:-5] Error
# a = test_string[::-1]
# a = test_string[::-1]
# print(a)

# modifying strings
#removing white-space

# test_string = " Hello, World! "
# print(test_string)

# print(test_string.strip())

#Replacing a pattern

# str1 = "Hello, HWorld!"
#
# str2 = str1.replace("H", "J")
# print(str2)

# test = "I!am$fine"
#
# test2 = test.split('$')
# print(test2)

#string formatting

# name = "Alice"
# age = 21

# temp = "{} is {} years old.".format(name, age)
# temp = f"{name} is {age} years old."
# print(temp)


# Escape characters

# print('This is Hla\'s laptop.')

# print("Printing a back-slash \\")

# print("Hello\rabc")
# print("Downloading.", end=" ")
# print("\r...")

# print("Hello\babc")

# print("\o101")
#
# li1 = ["hi", "i", "am", "fine"]
# li2 = " ".join(li1)
# print(li2)
# a = 5
# b = 4.5

# print(type(li1), type(a), type(b))
# if type(a) == int:
#     print("Hi")
# else:
#     print("Not hi")

# test_string = "Endoflife123漢字"
# # print(test_string.capitalize())
# print(len(test_string))
# print(test_string.center(14,"-"))
# print(test_string.count('file!'))

# print(test_string.encode("ascii", "ignore"))

# print(test_string.endswith("!"))
# # print(test_string.expandtabs(12))

# print(test_string.find('file'))

# print(test_string.isalnum())

# print(test_string.isascii())


# test_string = b"10101"
# print(test_string.isdecimal())

test_string = """Hello I am the file of the file. Are you?
Yes I am."""
print(len(test_string))

print(test_string.rfind("file"))

temp = test_string.splitlines()
print(temp)
print(type(temp))

temp1 = test_string.swapcase()

print(temp1.title())