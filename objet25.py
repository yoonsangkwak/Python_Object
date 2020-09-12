class BankAccount:
    """은행 계좌 클래스"""
    interest: float = 0.02

    def __init__(self, name: str, balance: float) -> None:
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드"""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄여주는 메소드"""
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def add_interest(self) -> None:
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance *= 1 + BankAccount.interest


# bank_account_1 = BankAccount("Hong Gildong", 1000)

# bank_account_1.add_interest()
# print(bank_account_1.balance)

# bank_account_1.deposit(500)
# print(bank_account_1.balance)

# bank_account_1.withdraw(2000)
# bank_account_1.withdraw(1000)
# print(bank_account_1.balance)

bank_account_2 = BankAccount("Hong Gildong", "1000")

print(bank_account_2.balance)
bank_account_2.deposit("00")
print(bank_account_2.balance)