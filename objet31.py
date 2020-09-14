class Cashier:
    """계산대 직원 클래스"""
    company_name = "코드잇 버거"    # 가게 이름
    raise_percentage = 1.03     # 시급 인상률
    burger_price = 4000     # 햄버거 가격

    def __init__(self, name, wage, number_sold=0):
        self.name = name    # 이름
        self.wage = wage    # 시급
        self.number_sold = number_sold  # 하루 판매량

    
    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= self.raise_percentage


    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다.")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change


    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name


jiwoong = Cashier("최지웅", 8900, 0)
jiwoong.raise_pay()
print(jiwoong.wage)
print(jiwoong.take_order(7000))
print(jiwoong.take_order(3000))
print(jiwoong.burger_price)
print(Cashier.burger_price)
print(jiwoong.number_sold)
print(jiwoong)