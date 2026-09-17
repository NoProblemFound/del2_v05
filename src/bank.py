from src.bankkonto import BankAccount

class Bank:
    def create_an_account(self):
        return BankAccount()

    def transfer(self, from_acc, to_acc, amount):
        if 0 < amount <= from_acc.balance:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print(f"{amount} kr överfördes.")
        else:
            print("Överföring misslyckades.")


