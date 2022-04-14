# input - True
# input - n (Number of lines) (if n = 4)
# *
# * *
# * * *
# * * * *

# input - False
# input - n (if n = 4)
# * * * *
# * * *
# * *
# *

f = open("temp.txt", "w")
a = """*
**
***"""
f.write(a)

f.close()

f = open("temp.txt", "r")
result = f.read()

f.close()