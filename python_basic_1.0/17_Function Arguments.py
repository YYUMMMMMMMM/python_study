# 함수 인자 : Function Arguments

'''
예제 1: 아래 함수가 실행 시 에러가 발생하는 이유를 생각, 함수 수정 후 정상적으로 실행

# 함수 선언
def greet(msg="Good morning!", name):
    return "Hi! " + name + ', ' + msg

# 실행
print(greet("Kim"))
print(greet("Park", "How do you do?"))
'''

# 기본값에 인자가 주어지는 함수를 만들 때
# 1. 모든 인자에 기본값을 주어야 함
# 2. 모든 인자에 기본값을 없애야 한다.
# 3. 디폴트값이 있는 인자를 뒤로 빼준다.

# 1. 모든 인자에 기본값을 주어야 함
# def greet(msg="Good morning!", name="Yeom"):
#     return "Hi! " + name + ', ' + msg
# print(greet("Kim"))
# print(greet("How do you do?", "Park"))

# 2. 모든 인자에 기본값을 없애야 한다. (인자 순서 중요)
# def greet(msg, name):
#     return "Hi! " + name + ', ' + msg
# print(greet("Bye", "Kim"))
# print(greet("How do you do?", "Park"))

# 3. 디폴트값이 있는 인자를 뒤로 빼준다.
# def greet(name, msg="Good morning!"):
#     return "Hi! " + name + ', ' + msg
# print(greet("Kim"))
# print(greet("Park", "How do you do?"))

# 파이썬 함수 인자 실행 순서는 중요
# 함수 정의시 가변인자, 기본값 등을 사용하면 활용도와 가독성이 높게 작성할 수 있다.
# 참고 : https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29

# 예제 2
# def add1(a, b=10, c=15):
#     print(a, b, c)
#     return a + b + c
# print(f'ex1 결과 : {add1(15)}')
# print(f'ex1 결과 : {add1(b=100, c=25, a=30)}') # 호출 시 매개변수 이름을 맞춰주면 순서는 상관 없다.

# 예제 3
def add2(*d):
    tot = 0
    for i in d: # iterable
        tot += i
    return tot
# print(f'ex2 결과 : {add2(10)}')
# print(f'ex2 결과 : {add2(10, 20)}')
# print(f'ex2 결과 : {add2(10, 20, 30)}')
# print(f'ex2 결과 : {add2(*(i for i in range(1, 101)))}')
# print(f'ex2 결과 : {add2((i for i in range(1, 101)))}')
# *가 없을 시 타입 에러가 떨어지는 이유
print(*(i for i in range(1, 101)))
print((i for i in range(1, 101)))

# 활용방안 : 최초 회원가입 시 포인트를 줄 때 디폴트값을 주면 된다.