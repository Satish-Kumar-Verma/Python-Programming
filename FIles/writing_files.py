
file = open("testing.txt", "w")

# input_text = input("Enter the string : ")

# methods for writing to a file
# f.write() , f.writelines()
# lines = input("Enter a list : ").split()

lines = input("Enter a list : ").split(",")
# file.write(input_text)
file.writelines(lines)

file.close()
