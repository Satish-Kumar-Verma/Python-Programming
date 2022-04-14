
file = open("testing.txt", "r+")

text = file.readlines()
print(text)

file.write("Hello, Why are you gay?\n")

file.close()