
file = open("hello.txt", 'r')

input_text = input("Enter a string : ")

# file.write("\n" + input_text + "\n")

# file.write(f"\n\n{input_text}\n")
temp = file.read()
print(temp)
file.close()
