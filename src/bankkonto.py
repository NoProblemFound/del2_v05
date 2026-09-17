class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Otillräckligt saldo.")

    def add_interest(self):
        self.balance *= 1.05

    def show_balance(self):
        print(f"Saldo: {self.balance:.2f} kr")