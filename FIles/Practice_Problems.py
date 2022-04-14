# No. 1

# input_char = input("Enter anything you want to write in a file : ")

# with open("temp.txt", 'w') as f:
#     f.write(input_char)
#

# No. 2

# one method
# try:
#     with open(input_char, "rt") as f:
#         print(f.read())
#
# except FileNotFoundError as e:
#     # print("File doesn't exist.")
#     print(e)

# another method

# import os
#
# if os.path.exists(f'{input_char}.txt'):
#     print("File is found!")
#
# else:
#     print("File is not found!")

# No.6


# with open("temp.txt", "rt") as f:
#     lines = f.readlines()
#     print(f"This files has {len(lines)} lines.")
#     words = 0
#     for line in lines:
#         words += len(line.split())
#     print(f"This file has {words} words!")
#     characters = 0
#     for line in lines:
#         characters += len(line)
#     print(f"This file has {characters} characters!")
#     print(lines)

# No.7


# with open("ar_kar_min.jpeg", 'rb') as f:
#     temp = f.read()
#
# with open("kwee_phyo.jpeg", 'wb') as f1:
#     f1.write(temp)

# No. 11



name = input("Enter your name : ")
phone_num = input("Enter your phone no : ")


with open('phone_book.bin', 'wb') as f:
    f.write(name.encode())
    f.write('\n'.encode())
    f.write(phone_num.encode())

with open('phone_book.bin', 'rb') as f:
    data = f.read()

print(data)