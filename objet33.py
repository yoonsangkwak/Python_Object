class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"    # 가게 이름
    raise_percentage = 1.03     # 시급 인상률

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name    # 이름
        self.wage = wage    # 시급


    def raise_pay(self):
        """시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage


    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    raise_percentage = 1.05

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold

    
    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name


class DeliveryMan(Employee):
    pass


young = Cashier("강영훈", 8900, 4)
print(young)
print(young.raise_percentage)