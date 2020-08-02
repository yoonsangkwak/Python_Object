class User:
    # 특수 메소드 (앞뒤로 _ 2개)
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
   
user1 = User("Young", "young@codeit.kr", "123456")


user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")


user3 = User("Taeho", "taeho@codeit.kr", "123abc")


user4 = User("Lisa", "lisa@codeit.kr", "abc123")




print(user1.name, user1.password)
print(user2.email, user2.password)
print(user3.name, user3.email)
print(user4.name, user4.email, user4.password)
