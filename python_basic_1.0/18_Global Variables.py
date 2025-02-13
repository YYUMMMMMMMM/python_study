# 전역변수 : Global Variables 

'''
예제 1: 아래 함수가 실행 시 에러가 발생하는 이유 를 생각, 함수 수정 후 정상적으로 실행

결과값 : 1000

# 전역변수
x = 100

def test():
    x = x * 10
    return x

print(test())
'''

def test():
    x = 100
    x = x * 10 # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
    return x
print(f'결과값 : {test()}')

# 파이썬 변수 스코프(영역)에 대한 이해는 정말 중요하다.
# 변수 영역에 대한 이해 부족 시 잘못된 결과값, 프로그램 종료 등 문제가 발생할 수 있다.
# 전역 변수 : 함수 내부가 아닌 외부에 정의되어 전체 범위를 갖는 변수 (프로그램 영역 전체, 함수 내부 엑세스 가능)
# 전역 변수의 변경, 수정(출력, 엑세스 X)이 필요한 경우는 global 키워드 사용

# 방법 1
x = 100

def test1():
    return x * 10
print(f'ex1 결과 : {test1()}')

# 방법 2
y = 100

def test2():
    # y = 100 # 지역변수로 선언해주거나
    global y # global 키워드 사용
    y *= 10 # UnboundLocalError: cannot access local variable 'y' where it is not associated with a value
    return y
print(f'ex2 결과 : {test2()}')