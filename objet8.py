class User:
    count = 0

    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1


user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# user1.count = 5
User.count = 5

print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)

# 같은 이름의 클래스 변수와 인스턴스 변수가있으면 인스턴스 변수가 읽어짐
# 클래스 변수에 값을 설정할 때는 클래스 이름만!