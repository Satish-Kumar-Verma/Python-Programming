from Person import Person
import pickle

# p = Person()
# p.set_name("Hla")
# p2 = Person()
# p2.set_name("Min")
# p3 = Person()
# p3.set_name("Naing")

# with open("Testing.dat", "wb") as f:
#     pickle.dump(p, f)
#     pickle.dump(p2, f)
#     pickle.dump(p3, f)

data = []
try:
    with open("Testing.dat", "rb") as f:
        while True:
            temp = pickle.load(f)
            data.append(temp)

except EOFError:
    pass

for item in data:
    print(item.get_name())
