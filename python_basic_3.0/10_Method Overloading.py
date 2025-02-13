"""
Chapter 02
Python Advanced(2) - Method Overloading
Keyword - Overloading, OOP, Multipledispatch

"""
"""
메소드 오버로딩 사용 이유
1. 동일 메소드 재정의
2. 네이밍으로 해당 메소드의 기능 예측이 가능
3. 코드 절약과 가독성 향상
4. 메소드 파라미터 기반 호출 방식 (오버라이딩과 차이점), 파라미터의 갯수에 따라서 알맞는 메소드를 호출

"""

# 예제 1 : 동일 이름 메소드 사용
# 동적 타입 검사 -> 런타임에 실행(타입 에러가 실행 시 발견된다.)

class SampleA:
    def add(self, x, y): # 해당 메소드는 에러 발생의 원인이 된다.
        return x + y
    def add(self, x, y, z):
        return x + y + z
    # 팩킹으로 해결 가능
    # def add(self, *args):
    #     return sum(args)

a = SampleA()
# print(f'Ex1 > {a.add(2, 4)}') # TypeError: SampleA.add() missing 1 required positional argument: 'z'
# print(f'Ex1 > {dir(a)}') # [..., 'add'] : 하나의 add 메소드 밖에 없다.

# 예제 2 : 동일 이름 메소드 사용 (legacy)

# 자료형에 따른 분기 처리
class SampleB:
    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args)
        elif datatype == 'str':
            return ''.join([x for x in args])
        
b = SampleB()

# 숫자 연산
print(f'Ex2 > {b.add('int', 5, 6)}') # 11

# 문자열 연산
print(f'Ex2 > {b.add('str', '5', '6')}') # 56

# 예제 3 : multipledispatch 패키지
# pip install multipledispatch

from multipledispatch import dispatch

class SampleC:
    @dispatch(int, int)
    def product(x, y):
        return x * y
    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z
    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z
    
c = SampleC()

# 정수 파라미터 2개
print(f'Ex3 > {c.product(2, 4)}') # 8
# 정수 파라미터 3개
print(f'Ex3 > {c.product(2, 4, 5)}') # 40
# 실수 파라미터 3개
print(f'Ex3 > {c.product(2.2, 4.4, 5.5)}') # 53.24000000000001
