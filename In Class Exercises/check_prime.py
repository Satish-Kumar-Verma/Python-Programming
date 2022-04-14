num = int(input("Enter a positive integer : "))
is_prime = False

if num == 2:
    print(f"{num} is a prime number.")

elif num > 2 or num == 1:

    while is_prime == False:
        half = int(num / 2)
        counter = 0
        for i in range(2, half):
            counter += 1
            if num % i == 0:
                is_prime = False
                break
        
        if counter == half - 2:
            is_prime = True
        
        break

    if is_prime is True:
        print(f"{num} is a prime number.")
    
    else:
        print(f"{num} is not a prime number.")

        
            