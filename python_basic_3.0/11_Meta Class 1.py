"""
Chapter 03
Python Advanced(3) - Meta Class 1
Keyword - Class of Class, Type, Meta Class, Custom Meta Class

"""
"""
메타 클래스
1. 클래스를 만드는 역할, 내가 의도하는 방향으로 클래스를 커스텀
2. 프레임워크 작성 시 필수
3. 동적 생성(type), 커스텀 생성(type) 함수
4. 커스텀 클래스 > 검증클래스, ...
5. 엄격한 Class 사용 요구, 메소드 오버라이드 요구

"""

# 예제 1 : type 예제
class SampleA: # 파이썬에서 Class == Object으로 이해하는 것이 좋다.
    pass

obj1 = SampleA() # 변수에 할당, 복사 가능, 새로운 속성, 함수의 인자로 넘기기 가능

# obj1은 SampleA의 인스턴스이다.
# SampleA의 메타클래스는 type
# type의 메타클래스는 type, type의 메타클래스는 자기 자신이다.
print(f'Ex1 > {obj1.__class__}') # <class '__main__.SampleA'>
print(f'Ex1 > {type(obj1)}') # <class '__main__.SampleA'>
print(f'Ex1 > {obj1.__class__ is type(obj1)}') # True

# SampleA의 메타(원형)는 뭘까? : 모든 클래스의 메타(원형) 클래스가 되는 것은 type 함수이다.
print(f'Ex1 > {obj1.__class__.__class__}') # <class 'type'>
print(f'Ex1 > {obj1.__class__.__class__ is type(obj1).__class__}') # True

# 핵심
print(type.__class__) # <class 'type'>

# 예제 2 : type meta (예제 1 증명)

# int, dict
n = 10
d = {'a' : 10, 'b' : 20}

class SampleB:
    pass

obj2 = SampleB()

for o in (n, d, obj2):
    print(f'Ex2 > {type(o)} {type(o) is o.__class__} {o.__class__.__class__}') # <class '__main__.SampleB'> True <class 'type'>

print()

for t in int, float, list, tuple:
    print(f'Ex2 > {type(t)}') # <class 'type'>

print(f'Ex2 > {type(type)}') # <class 'type'>



