"""
Chapter 02
Python Advanced(2) - Property 2 : Getter, Setter
Keyword - @property

"""
"""
프로퍼티(Property) 사용 장점
1. 파이써닉한 코드 작성
2. 변수 제약 설정 : 견고하고 내가 의도한대로 코드가 실행
3. Getter, Setter 효과 동등 (코드 일관성)
    - 캡슐화, 유효성 검사 기능 추가가 용이
    - 대체 표현 사용 (속성을 노출, 내부의 표현을 숨기기 가능)
    - 속성의 수명 및 메모리 관리가 용이
    - 디버깅 용이
    - Getter, Setter 작동에 대해 설계된 여러 라이브러리(오픈소스)가 있어 상호 운용성 증가

"""

# 예제 1 : @property를 활용하여 Getter, Setter 작성
class SampleA:
    def __init__(self):
        self.x = 0 # public
        self.__y = 0 # private
    # 이전 방식은 불편 private한 변수가 많아질 수록 get, set을 모두 만들어주어야하기 때문에 코드가 복잡해지고 불편하다.

    @property # Getter
    def y(self):
        print('Called get method.')
        return self.__y
    @y.setter # Setter
    def y(self, value):
        print('Called set method.')
        self.__y = value
    @y.deleter
    def y(self):
        print('Called del method.')
        del self.__y

a = SampleA()

a.x = 1
a.y = 2

print(f'Ex1 > x : {a.x}, y : {a.y}') # x : 1, y : 2

# deleter
# del a.y # _SampleA__y 삭제
print(f'Ex1 > ', dir(a))

# 예제 2 : @property 활용 제약 조건 추가
class SampleB:
    def __init__(self):
        self.x = 0 # public
        self.__y = 0 # private
    # 이전 방식은 불편 private한 변수가 많아질 수록 get, set을 모두 만들어주어야하기 때문에 코드가 복잡해지고 불편하다.

    @property # Getter
    def y(self):
        # print('Called get method.')
        return self.__y
    @y.setter # Setter
    def y(self, value):
        # print('Called set method.')
        if value < 0:
            raise ValueError('0보다 큰 값을 입력하세요.')
        self.__y = value
    @y.deleter
    def y(self):
        # print('Called del method.')
        del self.__y

b = SampleB()

b.x = 1
b.y = 10
# b.y = -10 # ValueError: 0보다 큰 값을 입력하세요.

print(f'Ex2 > x : {b.x}, y : {b.y}') # x : 1, y : 10
