
a = 10

b = 10
# b = a

print(id(a))
print(id(b))

if a is b:
    print("True")

else:
    print("False")