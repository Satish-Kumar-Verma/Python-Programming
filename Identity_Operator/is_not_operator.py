
a = int(input("Enter an integer : "))

b = int(input("Enter an integer : "))  #space vs time

print(id(a))
print(id(b))

if a is b:
    print("True")

elif a is not b:
    print("False")