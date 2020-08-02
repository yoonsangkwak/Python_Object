class User:
    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}")


    # Doubld Underscore (Dunder method)
    # 특정 상황에 자동으로 호출되는 method
    # print함수를 호출할때 자동으로됨
    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}, 비밀번호: *******"


user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "1q2w3e4r")

print(user1)
print(user2)