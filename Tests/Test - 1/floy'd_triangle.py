no_of_rows = int(input("Enter the number of rows : "))

numb = 1

for i in range(no_of_rows):
    for j in range(i + 1):
        print(numb, end="\t")
        numb += 1
    print()