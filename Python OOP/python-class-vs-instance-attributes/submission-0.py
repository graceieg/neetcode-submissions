class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    def __init__(self, name, balance) -> None:
        self.name = name
        self._balance = balance
        BankAccount.total_balance += balance
        BankAccount.total_accounts += 1

    

alice = BankAccount("Alice", 1000)
bob = BankAccount("Alice", 2000)

print(f"Alice's balance: ${alice._balance}")
print(f"Bob's balance: ${bob._balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
# TODO: Create two accounts
# TODO: Print the information using the mentioned format

