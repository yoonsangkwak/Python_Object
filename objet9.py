# 데코레이터 함수
def add_print_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper


@add_print_to    # 꾸며주라는 뜻 (데코레이터: 기존의 함수에 새로운 기능 추가!)
def print_hello():
    print("안녕하세요!")


print_hello()