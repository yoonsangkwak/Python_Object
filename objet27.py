class Citizen:
    """주민 클래스"""
    drinking_age = 19   # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self._age = age
        self._resident_id = resident_id


    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self._resident_id == id_field


    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age >= Citizen.drinking_age


    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self._age) + "살입니다!"


    @property   # getter 메소드
    def age(self):
        property("나이를 리턴합니다.")
        return self._age


    @age.setter # setter 메소드
    def age(self, value):
        print("나이를 설정합니다.")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
        else:
            self._age = value


young = Citizen("younghoon kang", 15, "12345678")
print(young.age)
young.age = 30
print(young.age)