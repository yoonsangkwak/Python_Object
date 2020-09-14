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
    burger_price = 4000

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold


    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다."""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    
    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name


class DeliveryMan(Employee):
    """배달원 클래스"""
    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원 복귀를 처리한다"""
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name


class CashierDeliveryMan(DeliveryMan, Cashier):
    def __init__(self, name, wage, on_standby, number_sold=0):
        Employee.__init__(self, name, wage)
        self.on_standby = on_standby
        self.number_sold = number_sold


cashier_and_delivery_man = CashierDeliveryMan("강영훈", 7000, True, 10)

cashier_and_delivery_man.take_order(3000)

cashier_and_delivery_man.deliver("코드잇 건물 101호")
cashier_and_delivery_man.deliver("코드잇 건물 102호")
cashier_and_delivery_man.back()

print(cashier_and_delivery_man)
print(CashierDeliveryMan.mro())