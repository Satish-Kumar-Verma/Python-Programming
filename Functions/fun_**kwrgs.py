

def personal_info(name, age, **kwargs):
    print(f"I am {name} and I am {age} years old.")
    print(f"Printing the **kwargs {kwargs}")
    print(f"Gender = {kwargs['gender']}")
    for key, value in kwargs.items():
        print(f"Key = {key}, value = {value}")

personal_info("alice", 15, gender="male", height="6")


