
# my_dictionary = {'name':'Alice', 'age':22, 'gender':'female', 'height':"58"}
# print(my_dictionary)

#length
# print(len(my_dictionary))

# check if a key is present in the dictionary

# if 'height' in my_dictionary:
#     print("Found")

#  Can a dictionary have duplicate keys?
#  NO!
# print(my_dictionary)

# temp = {'name': "Alice", 'age':22}
# print(temp)

# getting the key-value pairs
# for key, value in my_dictionary.items():
#     print(f"Key = {key}")
#     print(f"Value = {value}")

# print(my_dictionary.keys())
# print(my_dictionary.values())

# temp_dict = {'uni':'MIIT'}
#
# my_dictionary.update(temp_dict)
# print(my_dictionary)

# print(my_dictionary.pop('uni'))
# print(my_dictionary)

# print(my_dictionary.setdefault('location', 'Mandalay'))
# print(my_dictionary)

# No. 1
# emp_details = {}
# Printing the details of the employee :
# Name : Alice
# Age : 22
# Year of Experience : 4
# Address : Mandalay
# Phone No. : 091234567890

# emp_details = {'name' : input("Enter your name : "), 'age' : int(input("Enter your age : "))}
#
# print("Printing the employee details : ")
# keys = list(emp_details.keys())
# print(f"Keys : {keys}")
#
# values = list(emp_details.values())
# print(f"Values : {values}")
#
# key_values = list(emp_details.items())
# print(f"Key-Values : {key_values}")

# for key, value in emp_details.items():
#     print(f"{key} : {value}")


# No.3

# dict = {1 : 1, 2 : 2, 3 : 3}
# total = 0
# for value in dict.values():
#     total += value
#
# print(total)
# print(sum(dict.values()))

# No.4

# length = int(input("How many items do you want in the dictionary : "))
# my_dict = {}
# for i in range(length):
#     key = input("Enter the key : ")
#     value = input("Enter the value : ")
#     my_dict.update({key : value})
#
# for key, value in my_dict.items():
#     print(f"{key} : {value}")

# No. 5

# no_of_players = int(input("Enter the number of players : "))
# players = {}
# temp = []
# for i in range(no_of_players):
#     detail = input("Enter your name and score in the given format [name=score] : ").split("=")
#     temp.append(detail)
#
# print(temp)
#
# players = dict(temp)
# print(players)
# while True:
#     name = input("Enter the player's name to retrive the score : ")
#     if name in players.keys():
#         break
# print(players[name])

# No.6

# my_dict = {'hla': '100', 'khant': '120', 'ar': '130'}
#
# for key, value in my_dict.items():
#     print(f"{key} : {value}")

# my_dict = {'p1' : 'hla min naing', 'p2' : 'ar kar min', 'p3' : 'khant pyae phyo'}
#
# while True:
#     x = input("Enter the character you want to count : ")
#     if x == "exit":
#         break
#
#     for i in range(len(my_dict)):
#         count = my_dict[f'p{i + 1}'].count(x)
#         print(f"Count for {x} : {count}")

# No.8

# my_dict = {'p3' : 'hla min naing', 'p2' : 'ar kar min', 'p1' : 'khant pyae phyo'}
#
# # sorting with keys
# my_dict = sorted(my_dict.items(), key=lambda x : x[0])
# my_dict = dict(my_dict)
# print(my_dict)


# sorting with values

# _dict = sorted(my_dict.items(), key=lambda x : x[1])
# my_dict = dict(my_dict)
# print(my_dict)

# No.9

# my_dict = {'p3' : 'hla min naing', 'p2' : 'ar kar min', 'p1' : 'khant pyae phyo'}

# del my_dict['p2']
# my_dict.pop('p2')
# print(my_dict)

# No.10

# keys = "p1 p2 p3 p4".split()
#
# values = "Hla Min Naing, Ar Kar Min, Khant Pyae Phyo, Ying".split(",")
#
# print(keys)
# print(values)
#
# print(f"Zip output : {list(zip(keys, values))}")
# my_dict = dict(zip(keys, values))
# print(my_dict)

# No.11

# input_str = "p1=hla p2=khant p3=ar"
#
# my_list = []
#
# for item in input_str.split():
#     temp = item.split("=")
#     print(f"Temp : {temp}")
#     my_list.append(temp)
#
# print(f"My List = {my_list}")
# my_dict = dict(my_list)
#
# for key, value in my_dict.items():
#     print(f"{key} : {value}")

# NO.12
# Just SKIPPPPP! It's TOO EASY!

# No. 13

# from collections import OrderedDict
# # import collections
# d = OrderedDict()
# d[1] = 'Hello'
# d[2] = "hi"
# d[3] = "xi"
# print(d)
