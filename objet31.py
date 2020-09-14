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


class DeliveryMan:
    """배달원 클래스"""
    company_name = "코드잇 버거"    # 가게 이름
    raise_percentage = 1.03     # 시급 인상률

    def __init__(self, name, wage, on_standby):
        self.name = name    # 이름
        self.wage = wage    # 시급
        self.on_standby = on_standby    # 대기 상태


    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= self.raise_percentage


    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 설명 메세지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")


    def back(self):
        """배달원을 복귀 처리한다"""
        self.on_standby = True


    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name


taeho = DeliveryMan("성태호", 7000, True)

taeho.raise_pay()
print(taeho.wage)

taeho.deliver("서울시 코드잇로 51 최고 건물 401호")
taeho.deliver("서울시 코드잇로 51 최고 건물 402호")

taeho.back()
taeho.deliver("서울시 코드잇로 51 최고 건물 402호")

print(taeho)