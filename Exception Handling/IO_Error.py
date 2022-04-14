

try:
    with open("temp.txt", 'r') as f:
        data = f.read()
        print(data)

except IOError as e:
    print("File Not found!")

finally:
    print("Bye Bye!")
