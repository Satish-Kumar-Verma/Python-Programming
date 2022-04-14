# range(start, stop, stepping) stop = 5 ---> will stop at 4

def reverse_gen(my_str):
    for i in range(len(my_str) - 1, -1, -1):
        yield my_str[i]


# for i in reverse_gen("Hello"):
#     print(i)

a = reverse_gen("Hello")
for i in a:
    print(i)

b = "hello"
# b = b[::-1]
b = "".join(reversed(b))  # I have never seen this in my LIFE!!! (AKM)

print(b)
