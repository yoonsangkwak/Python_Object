class User:
    # initialize 메소드를 여기 쓰세요
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# 인스턴스를 통해서 인스턴스 메소드 호출        
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

# 클래스를 통해서 인스턴스 메소드 호출
user3 = User()
User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
User.initialize(user4, "Lisa", "lisa@codeit.kr", "abc123")



print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
