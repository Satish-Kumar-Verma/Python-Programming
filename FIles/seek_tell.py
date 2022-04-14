
f = open("hello.txt", "rt")

# TO count the number of characters in a file
# while True:
#     temp = f.readline()
#     if len(temp) == 0:
#         print(f.tell())
#         break
#     else:
#         print(temp)

# Seek Function

print(f.readlines())
f.seek(12)
print(f.readline())
print(f.tell())
f.close()