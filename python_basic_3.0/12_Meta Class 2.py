"""
Chapter 03
Python Advanced(3) - Meta Class 2
Keyword - type(name, base, dct), Dynamic Metaclass

"""
"""
메타클래스 사용 이점
1. 메타클래스 동적 생성 중요
2. 동적 생성한 메타클래스는 커스텀 메타클래스를 생성할 수 있다.
3. 의도하는 방향으로 직접 클래스 생성에 관련할 수 있는 큰 장점이 있다.

"""

# 예제 1 : type 동적 클래스 생성 예제
# type() 함수는 세 개의 인자를 받는다.
# name(이름), bases(상속), dct(속성, 메소드)

class Sample1:
    pass

s1 = type('Sample1', (), {}) # 위와 같은 형태
print('Ex1 > ', s1) # <class '__main__.Sample1'>
print('Ex1 > ', type(s1)) # <class 'type'>
print('Ex1 > ', s1.__base__) # <class 'object'>
print('Ex1 > ', s1.__dict__)

# 예제 2 : 동적 생성 + 상속
class Parent1:
    pass

class Sample2(Parent1):
    attr1 = 100
    attr2 = 'Hi'

s2 = type('Sample2', (Parent1,), dict(attr1=100, attr2='Hi'))
# TypeError: type.__new__() argument 2 must be tuple, not type : base는 두 개의 인자를 받아야 한다.
print('Ex2 > ', s2) # <class '__main__.Sample2'>
print('Ex2 > ', type(s2)) # <class 'type'>
print('Ex2 > ', s2.__base__) # <class '__main__.Parent1'>
print('Ex2 > ', s2.__dict__) # {'attr1': 100, 'attr2': 'Hi', '__module__': '__main__', '__doc__': None}
print('Ex2 > ', s2.attr1, s2.attr2) # 100 Hi

# 예제 3 : type 동적 클래스 생성 + 메소드
class SampleEx:
    attr1 = 30
    attr2 = 100
    def add(self, m, n):
        return m + n
    def mul(self, m, n):
        return m * n
    
ex = SampleEx()

print('Ex3 > ', ex.attr1)
print('Ex3 > ', ex.attr2)
print('Ex3 > ', ex.add(100, 200))
print('Ex3 > ', ex.mul(100, 200))

s3 = type(
    'SampleEx',
    (object,),
    {'attr1' : 30, 'attr2' : 100, 'add' : lambda x, y : x + y, 'mul' : lambda x, y : x * y}
)   # dict(attr1=30, attr2=100, add=lambda x, y: x + y, mul=lambda x, y : x * y)

print('Ex3 > ', s3.attr1)
print('Ex3 > ', s3.attr2)
print('Ex3 > ', s3.add(100, 200))
print('Ex3 > ', s3.mul(100, 200))