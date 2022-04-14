a = b'5'
my_str = b"Hello world!"
my_list = [1, 2, 3, 4, 5]

with open("hello.bin", "wb") as f:
    f.write(bytearray(my_list))

with open("hello.bin", "rb") as f:
    temp = f.read()
print(list(temp))
