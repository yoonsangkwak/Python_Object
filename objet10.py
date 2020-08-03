class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print(f"안녕하세요! 저는{self.name}")

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}, 비밀번호: ******"

    @classmethod
    def number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다.")

    # def number_of_users(self):
    #     print(f"총 유저 수는: {User.count}입니다.")

user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 클래스 메소드 사용 (인스턴스 변수가 하나도 없어도 사용가능)
User.number_of_users()
# user1.number_of_users()