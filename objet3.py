class User:
    def say_hello(self):
        # 인사 메세지 출력 메소드
        print(f"안녕하세요! 저는 {self.name}입니다.")

    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        return self.name == name


user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "이회중"
user2.email = "hoijoong@codeit.kr"
user2.password = "34567"

user3.name = "엄준식"
user3.email = "isalive@codeit.kr"
user3.password = "67875"

print(user1.check_name("김대위"))
print(user1.check_name("이회중"))