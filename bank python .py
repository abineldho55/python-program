class bank:
    def __init__(self, accno, name, ac_type, bal):
        self.accno = accno
        self.name = name
        self.ac_type = ac_type
        self.bal = bal

    def display(self):
        print("\nAccount info:")
        print("Account number:", self.accno)
        print("Account name:", self.name)
        print("Account type:", self.ac_type)
        print("Account balance:", self.bal)

    def deposit(self):
        dep = int(input("Enter amount to deposit: "))
        self.bal = self.bal + dep

    def withdraw(self):
        w = int(input("Enter amount to withdraw: "))
        if w > self.bal:
            print("Insufficient Balance")
        else:
            self.bal = self.bal - w
            print("Rs", w, "Successfully Withdrawn")

b1 = bank(0, '', '', 0) # Initialize an instance of the bank class with default values

while True:
    print("\n1. Account info\n2. Deposit\n3. Withdraw\n4. Exit")
    opt = int(input("Select your option: "))

    if opt == 1:
        b1.display()
    elif opt == 2:
        b1.deposit()
    elif opt == 3:
        b1.withdraw()
    elif opt == 4:
        print("Exit")
        break
    else:
        print("Invalid Option")