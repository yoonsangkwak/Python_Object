print(max(2, 5))             # => 5
print(max(2, 7, 5))          # => 7
print(min(2, 5))             # => 2
print(min(2, 7, 5, 11, 6))   # => 2

# max 함수는 파라미터 중 가장 큰 값을, 
# min 함수는 파라미터 중 가장 작은 값을 리턴합니다. 
# 두 함수 모두 원하는 개수만큼의 파라미터들을 넘겨줄 수 있습니다.

int_list = [1, 2, 3, 4, 5]
int_tuple = (4, 3, 6, 1, 2)
int_dict = {1: "one", 2: "two", 3: "three"}
    
print(sum(int_list))         # => 15
print(sum(int_tuple))        # => 16
print(sum(int_dict))         # => 6

# sum 함수는 리스트, 튜플, 딕셔너리에 있는 숫자형 요소들의 합을 리턴합니다. 
# sum 함수에 딕셔너리를 파라미터로 넘기면 key들의 합을 리턴합니다.

condition = True
    
if condition:
    condition_string = "nice"
else:
    condition_string = "not nice"
    
print(condition_string)      # => nice

###############    ternary expression   #################

condition = True
    
condition_string = "nice" if condition else "not nice"
    
print(condition_string)      # => nice

'''
위의 코드와 아래의 코드는 같은 내용입니다. 
"nice" if condition else "not_nice" 이 구문은
condition이 True 일 때는 "nice"가 되고
False 일 때는 "not_nice"가 된다는 뜻입니다.
이렇게 불린(Boolean) 값에 따라 다른 값을 리턴하는 구문을 ternary expression이라고 합니다. 
ternary expression을 사용하면 if, else로 복잡하게 표현해야 하는 구문을 간단하게 나타낼 수 있습니다
'''

int_list = [1, 2, 3, 4, 5, 6]
squares = []
    
for x in int_list:
    squares.append(x**2)
    
print(squares)               # [1, 4, 9, 16, 25, 36]

########    list comprehension    ########

int_list = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in int_list]
    
print(squares)               # [1, 4, 9, 16, 25, 36]

'''
위 코드와 아래 코드는 같은 뜻입니다. 
list comprehension은 새로운 리스트를 만드는 간편한 방법입니다. 
특정 리스트나 튜플을 바탕으로 리스트를 생성할 때
[] 안에 원하는 값을 리턴하는 식 (x**2) 뒤에
for문을 써줍니다(for x in int_list).
이렇게 쓰면 int_list 의 각 요소들을 제곱해준 값들로 
이루어진 새로운 리스트가 생성됩니다.
'''

# zfill
print("1".zfill(6))   # 000001
print("333".zfill(2))  # 333
print("a".zfill(8))  # 0000000a
print("ab".zfill(8))  # 000000ab
print("abc".zfill(8))  # 00000abc

'''
이 메소드는 문자열을 최소 몇 자리 이상을 가진 문자열로 변환시켜줍니다. 
이때 만약 모자란 부분은 왼쪽에 “0”을 채워주는데요. 
예를 들어 만약 "1".zfill(2)을 하면 "01"을 리턴합니다. 
그리고 설정된 자릿수보다 이미 더 긴 문자열이라면 그 문자열을 그대로 출력합니다. 
그러니까 "333".zfill(2) 와 같이 하면 문자열 그대로 “333”을 리턴합니다. 
이 메소드는 문자열을 예쁘고 통일감있게 출력하고자 할 때 자주 사용되니까 꼭 기억해주세요.
'''

# rjust & ljust
test1 = "12345".rjust(10, "k")
print(test1)
# 출력
# kkkkk12345

test2 = "12345".ljust(10, "k")
print(test2)
# 출력
# 12345kkkkk