# student_info = {}

# for i in range(10):
#     name = input("Enter the student's name : ")
def get_the_minimum_five(dict_):
    values = list(dict_.values())
    values = sorted(values, reverse=True)
    print(values)
    index = 5

    for i in range(5):
        for key, value in dict_.items():
            if index < 10:
                if dict_[key] == values[index]:
                    print(f"Name : {key}")
                    print(f"Marks : {value}")
                    index += 1





students = "A B C D E F G H I J".split()
marks = list(map(int, "1 2 3 4 5 6 7 8 9 10".split()))

student_info = dict(zip(students, marks))

print(student_info)

get_the_minimum_five(student_info)