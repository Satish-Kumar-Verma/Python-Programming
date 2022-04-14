

# Bank networks - JCB, MPU
# Foreign Bank networks - Visa, Mastercard, UnionPay
# Cards - KBZ (MPU), CB(JCB, MPU), AYA(JCB), AGD(MPU)

# KBZ - ATM (MPU, Visa)

class Visa(object):
    def __init__(self):
        self.visa_withdraw()
        super().__init__()

    def visa_withdraw(self):
        print("Visa Operation Successful!")


class MasterCard(object):
    def __init__(self):
        self.master_withdraw()
        super().__init__()

    def master_withdraw(self):
        print("Master Operation Successful!")


class ATM(Visa, MasterCard):
    def __init__(self):
        super().__init__()
        temp = input("Deposite or withdrawl : ")
        print(temp)


atm = ATM()
