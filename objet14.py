'''
mutable_object = [1, 2, 3] # 리스트는 가변타입
immutable_object = (1, 2, 3) # 튜플은 불변타입

mutable_object[0] = 4
print(mutable_object)

immutable_object[0] = 4
print(immutable_object)
# 불변타입 : 변수가 가리키는 객체 자체는 바꿀 수 있음
'''

tuple_x = (6, 4)
tuple_x = (4, 1)
tuple_x = (4, 1, 7)

print(tuple_x)

list_x = []
list_x.append(4)
list_x.append(1)
list_x.append(7)

print(list_x)

# 리스트와 딕셔너리는 가변
# 불린 정수 실수 문자열 튜플은 불변
# 직접 작성하는 클래스는 가변타입