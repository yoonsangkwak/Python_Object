# 우사인 볼트의 평균 속도 = 10.438413361 m/s
bolt_speed = 10.438413361
minute = 60

print(bolt_speed * minute)  # 1분(60초) 동안 간 거리
print(bolt_speed * 2 * minute)  # 2분(120초) 동안 간 거리
print(bolt_speed * 3 * minute)  # 3분(180초) 동안 간 거리


# 함수 추상화
def welcome(name):
    print("Hello, " + name)
    print("Welcome to Codeit!")


welcome("영훈")
welcome("규식")
welcome("대위")


# []를 이용해서 빈 리스트 인스턴스를 정의한다
example_list = []
example_list.append(3)
example_list.append(2)
example_list.append(6)
print(example_list[0])
print(example_list[1])
print(example_list[2])