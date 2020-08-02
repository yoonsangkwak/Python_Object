class User:
    def say_hello(self):
        # 인사 메세지 출력 메소드
        print(f"안녕하세요! 저는 {self.name}입니다!")
    
    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호 입니다.")


user1 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

# user1.login(user1, "captain@codeit.kr", "12345") # user1이 자동으로 첫번째 파라미터로 감
user1.login("captain@codeit.kr", "12345")