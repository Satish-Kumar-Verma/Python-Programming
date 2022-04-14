
def remove_last(s):
    return s.strip()

input_str = input("Enter a string : ").split(",")

# print(input_str)
# print(remove_last(input_str[0]))
# result = []
# for item in input_str:
#     result.append(remove_last(item))
#
# print(result)
print(input_str)
input_str = list(map(lambda i : i.strip(), input_str))
print(input_str)