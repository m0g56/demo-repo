class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount


if __name__ == "__main__":
    account = BankAccount("Alex", 100.0)
    account.deposit(50.0)
    print(f"{account.owner}'s balance is ${account.balance:.2f}")
