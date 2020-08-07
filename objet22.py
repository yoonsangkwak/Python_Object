# 추상화의 안 좋은 예시
# 어디에 쓰는 클래스인지 이해하기 힘들다

class SomeClass:
    class_variable = 0.02

    def __init__(self, variable_1, variable_2):
        self.variable_1 = variable_1
        self.variable_2 = variable_2

    def method_1(self, some_value):
        self.variable_2 += some_value

    def method_2(self, some_value):
        if self.variable_2 < some_value:
            print("Insufficient balance!")
        else:
            self.variable_2 -= some_value

    def method_3(self):
        self.variable_2 *= 1 + SomeClass.class_variable

# 추상화의 좋은 예시
# 어디에 쓰는 클래스인고 어떻게 사용할지 직관적으로 알 수 있다

class BankAccount:
    interest = 0.02

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def add_interest(self):
        self.balance *= 1 + BankAccount.interest


example_account = BankAccount("Hong Gil dong", 1000)
example_account.add_interest()
print(example_account.balance)

example_account.deposit(500)
print(example_account.balance)

example_account.withdraw(2000)
example_account.withdraw(1000)
print(example_account.balance)