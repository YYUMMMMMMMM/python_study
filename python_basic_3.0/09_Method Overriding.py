"""
Chapter 02
Python Advanced(2) - Method Overriding
Keyword - Overriding, OOP, 다형성

"""
"""
메소드 오버라이딩 사용 이유
1. 서브 클래스(자식 클래스)에서 슈퍼 클래스(부모 클래스)를 호출 후 사용
2. 메소드 재정의 후 사용 가능
3. 부모클래스의 메소드를 추상화 후 사용 가능 (구조적 접근 가능)
4. 확장 가능, 다형성(다양한 방식으로 동작)
5. 가독성 증가, 오류 가능성 감소, 메소드 이름 절약, 유지보수성 증가, ...

"""

# 예제 1 : 기본 Overriding
class ParentEx1:
    def __init__(self):
        self.value = 5
    def get_value(self):
        return self.value

class ChildEx1(ParentEx1):
    pass

c1 = ChildEx1()
p1 = ParentEx1()

# 부모클래스 메소드 호출
print(f'Ex1 > {c1.get_value()}') # 5

# c1 모든 속성 출력
print(f'Ex1 > {dir(c1)}') # [..., 'get_value', 'value']

# 부모와 자식의 모든 속성 출력
print(f'Ex1 > {dir(ParentEx1)}') # [..., 'get_value', 'value']
print(f'Ex1 > {dir(ChildEx1)}') # [..., 'get_value', 'value']

print()
print()

print(f'Ex1 > {ParentEx1.__dict__}')
# {'__module__': '__main__', '__firstlineno__': 18, '__init__': <function ParentEx1.__init__ at 0x0000024E28231440>, 'get_value': <function ParentEx1.get_value at 0x0000024E28444680>, '__static_attributes__': ('value',), '__dict__': <attribute '__dict__' of 'ParentEx1' objects>, '__weakref__': <attribute '__weakref__' of 'ParentEx1' objects>, '__doc__': None}
print(f'Ex1 > {ChildEx1.__dict__}')
# {'__module__': '__main__', '__firstlineno__': 24, '__static_attributes__': (), '__doc__': None}

# 예제 2 : 기본 Overriding 메소드 재정의
class ParentEx2:
    def __init__(self):
        self.value = 5
    def get_value(self):
        return self.value

class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10

c2 = ChildEx2()
print(f'Ex2 > {c2.get_value()}') # 50
p2 = ParentEx2()
print(f'Ex2 > {p2.get_value()}') # 5

# 예제 3 : Overriding 다형성 예제
import datetime

class Logger:
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now(), msg=msg)
        super(TimestampLogger, self).log(message)
        # super().log(message)

class DateLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().strftime('%Y=%m-%d'), msg=msg)
        # super(DateLogger, self).log(message)
        super().log(message)

l = Logger()
t = TimestampLogger()
d = DateLogger()

l.log('Called logger')
t.log('Called timestamp logger')
d.log('Called date logger')