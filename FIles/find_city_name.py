# with open("city_names.bin", 'rb') as f:
#     data = f.read()
#
# city_name = input("Enter the city name : ")
# data = data.decode().split('\n')
# for i in range(len(data)):
#     if data[i] == city_name:
#         print("We found the city in the database!")
#         print(f"Record Number : {i + 1}")
#         break
# else:
#     print("We didn't find the city name!")


# No. 13

with open("city_names.bin", "rb") as f:
    data = f.read()

data = data.decode().split('\n')

print(f"The file has {len(data)} records.")

index = int(input("Which one do you want to modify or delete : "))
index -= 1

input_data = input("Enter the data to modify [type delete to delete the data] : ")

if input_data.lower() == 'delete':
    data.pop(index)

else:
    data[index] = input_data

print(data)

with open('city_names.bin', 'wb') as f:
    for item in data:
        f.write(item.encode())
        f.write('\n'.encode())

