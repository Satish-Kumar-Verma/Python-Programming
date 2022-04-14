
try:
    f = open("Hello.txt", "a+")
    f.write("Hello\n")
    f.seek(0)
    print(f.read())

except FileNotFoundError as e:
    print("The file doesn't exist!")
    print(e)