

name = input("Enter your name : ")

age = int(input("Enter your age : "))

gender = input("Male/Female : ")

ph_no = int(input("Enter your phone number : "))

address = input("Enter your address : ")

height = input("Enter your height : ")

print(f"I am {name}({gender}). I live in {address}. I am {age} years old. My height is {height}.\nContact info : 0{ph_no}.") # using f-string

print("I am " + name + "(" + gender + "). I live in " + address + ". I am " + str(age) + " years old. My height is " + height + ".\nContact info : 0" + str(ph_no) +".")
