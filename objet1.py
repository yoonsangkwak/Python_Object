class User:
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다.")


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

User.say_hello(user1)
user1.say_hello()