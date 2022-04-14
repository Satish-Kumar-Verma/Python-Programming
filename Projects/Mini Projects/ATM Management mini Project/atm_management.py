

balance = 10000
print("1.Deposite \n2.Withdrawl \n3.Balance inquiry \n4.Exit ?")
choice = int(input("Enter your choice : "))


if choice == 1:
    deposite_amt = int(input("Enter the amount to deposite : "))

    balance += deposite_amt

    print(f"Your A/c xxxxxxxxxxxxxx983 Credited by $:{deposite_amt}, available balance : {balance}")


elif choice == 2:
    withdrawl_amt = int(input("Enter the amount to withdraw : "))

    if balance - withdrawl_amt >= 100:
        balance -= withdrawl_amt
        print(f"Your A/c xxxxxxxxxxxxx983 Debited by $:{withdrawl_amt}, available balance : {balance}")

    else:
        print("Insufficient balance!")
        print(f"Available balance : {balance}")


elif choice == 3:
    print(f"Available balance : {balance}")

elif choice == 4:
    print("Thanks for using KKK's ATM service!\nHave a nice day!")

else:
    print("Wrong choice!")

