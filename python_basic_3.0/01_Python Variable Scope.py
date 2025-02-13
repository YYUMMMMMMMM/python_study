"""
Chapter 01
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals

"""
"""
전역변수는 주로 변하지 않는 고정 값(상수)에 사용한다.
지역변수의 사용 이유 : 지역변수는 함수 내에 로직 해결에 국한, 소멸주기 : 함수 실행 해제 시
전역변수를 지역 내에서 수정하는 것은 권장되지 않는다.

"""

# 예제 1
a = 10 # Global variable

def foo():
    # Read global variable
    print('Ex1 > ', a)

foo()

# Read global variable
print('Ex1 > ', a)

# 예제 2
b = 20

def bar():
    b = 30 # Local variable
    print('Ex2 > ', b) # Read local variable : 함수 안에서 변수를 찾을 때 로컬 스코프 안에서 먼저 찾는다.

bar() # 30
print('Ex2 > ', b) # 20

# 예제 3
c = 40

def foobar():
    # c = c + 10 # UnboundLocalError
    # c = 10
    # c += 100
    print('Ex3 > ', c) # local variable

foobar()

# 예제 4
d = 50

def barfoo():
    global d # global : 전역 스코프에 선언된 변수(전역 변수)를 읽고, 수정 가능하다.
    d = 60
    d += 100
    print('Ex4 > ', d)

barfoo() # 160
print('Ex4 > ', d) # 160

# 예제 5, 중요!
# Closure pattern
def outer():
    e = 70
    def inner():
        nonlocal e # nonlocal : 지역변수끼리의 입력, 수정이 가능
        e += 10 # UnboundLocalError
        print('Ex5 > ', e)
    return inner

in_test = outer() # Closure
in_test() # 80
in_test() # 90 : Closure 이기 때문에 함수의 호출이 끝나도 데이터를 기억하고 있다.

# 예제 6
def func(var):
    x = 10
    def printer():
        print('Ex6 > ', "Printer Func Inner")
    print("Func Inner", locals())
    # Func Inner {'var': 'Hi', 'x': 10, 'printer': <function func.<locals>.printer at 0x0000019FAFCAC540>}
    # locals() : 호출 시 해당 로컬 영역안에 있는 모든 것들을 딕셔너리로 출력
func('Hi')

# 예제 7
print('Ex7 > ', globals())
# globals() : 호출 시 전역 있는 모든 것들을 딕셔너리로 출력
globals()['test_variable'] = 100
print('Ex7 > ', globals())

# 예제 8 (지역 > 전역 변수 생성)
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k
# print(globals())
# print('Ex8 > ', plus_5_5) # Ex8 >  10
# print('Ex8 > ', plus_9_9) # Ex8 >  18