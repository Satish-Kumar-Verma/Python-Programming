
# three methods of reading
# f.read(), f.readline(), f.readlines()

file = open("/home/sonu/Desktop/temp.txt", "r")

text = file.read(6)  # you can specify the number of characters to read. If you don't, it will read everything
# stored in the file.

# text = file.readline()
# text = file.readlines()
print(text)

file.close()
