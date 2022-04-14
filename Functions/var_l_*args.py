
def personal_info(name, age, *args):
    print(f"I am {name} and I am {age} years old.")
    print(f"Printing the *args {args}")

personal_info("alice", 15, "female", "6")


