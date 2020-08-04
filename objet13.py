class User:
    count = 0
    
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
    
        User.count += 1
    
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))
    
user1 = User("Young", "young@codeit.kr", "12345")

print(type(user1))

print(type(2))
print(type("string"))
print(type([]))
print(type({}))
print(type(()))

def print_hello():
    print("안녕하세요!")

print(type(print_hello))

int_list = []
int_list.append(1) # 리스트 클래스의 append 메소드
int_list.append(3)
int_list.append(7)

print(int_list)

'''
1 # int 클래스로 만든 1을 나타내는 인스턴스 생성
"" # 문자열 클래스로 만든 빈 문자열을 나타내는 인스턴스 생성
'''