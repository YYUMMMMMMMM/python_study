# Chapter03_02 파이썬 데이터 모델
# special method(magic method)
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(functions), 클래스(class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 클래스 예제 2
# 벡터(x,y)
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class Vector(object): # object 굳이 명시해주지 않아도 됨
    def __init__(self, *args):
        """
        Create a vector, example : v = Vector(5, 10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
    
    def __repr__(self):
        """
        Return the vector information.
        """
        return 'Vector(%r, %r)' % (self._x, self._y)
    
    def __add__(self, other):
        """
        Return the vector addtion of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)
    
    def __bool__(self):
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 30)
v3 = Vector()

# 매직 메소드 출력
# print(Vector.__init__.__doc__)
# print(Vector.__repr__.__doc__)
# print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))