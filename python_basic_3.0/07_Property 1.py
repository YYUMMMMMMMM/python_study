"""
Chapter 02
Python Advanced(2) - Property 1 : Underscore
Keyword - access modifier(접근지정자), underscore

"""
"""
다양한 언더스코어 사용
접근지정자 이해

"""

# 예제 1 : Use Underscore
# 1. 인터프리터, 2. 값 무시, 3. 네이밍(국제화, 자릿수)

# Unpacking
x, _, y = (1, 2, 3)
# print(x, y) # 1, 3 (2는 무시)

a, *_, b = (1, 2, 3, 4, 5)
# print(a, b) # 1, 5 (2, 3, 4 모두 무시)

print('Ex1 > ', x, y, a, b)

for _ in range(10):
    pass # 값을 사용하는 것이 아니라 어떠한 로직 자체를 반복하고 싶을 때도 사용 가능

for _, val in enumerate(range(10)):
    pass

# 예제 2 : 접근지정자
# name : public
# _name : protected
# __name : private
# 파이썬에서 public 강제X, 약속된 규약에 따라 코딩을 장려한다. (자유도, 책임감 장려)
# 타 클래스에서 클래스 변수, 인스턴스 변수 값을 쓰기를 장려하지 않는다. > Naming Mangling
# 타 클래스에서 __name 의 변수는 접근하지 않는 것이 원칙이다.

# No use property
class SampleA:
    def __init__(self):
        self.x = 0 # public
        self.__y = 0 # private
        self._z = 0 # protected

a = SampleA()

a.x = 1
print('Ex2 > x : {}'.format(a.x)) # 1
# print('Ex2 > y : {}'.format(a.__y)) # AttributeError: 'SampleA' object has no attribute '__y'
print('Ex2 > z : {}'.format(a._z)) # 0

print('Ex2 > ', dir(a)) # ['_SampleA__y', ..., '_z', 'x'], y가 _SampleA__y 변함
a._SampleA__y = 2
print('Ex2 > y : {}'.format(a._SampleA__y)) # 2, 직접적으로 접근하여 강제로 수정은 가능하지만 약속된 규약을 지켜야 한다.

# 예제 3 : 메소드 활용 Getter, Setter

class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0 # _SampleB__y
    def get_y(self):
        return self.__y
    def set_y(self, value):
        self.__y = value

b = SampleB()

b.x = 1
b.set_y(1)

print('Ex3 > x : {}, y : {}'.format(b.x, b.get_y())) # x : 1, y : 1

# 변수 접근 후 수정 부분에서 일관성 및 가독성이 하락한다.
# b.SampleB__y = 343

print('Ex3 > ', dir(b)) # ['_SampleB__y', ...,  'get_y', 'set_y', 'x']