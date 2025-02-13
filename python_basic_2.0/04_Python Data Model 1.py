# Chapter03_01 파이썬 데이터 모델
# special method(magic method)
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(functions), 클래스(class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 3+3을 했을 때 파이썬 내부적으로 어떤 메소드가 실행될까

# 기본형
print(int) # <class 'int'>
print(float) # <class 'float'>

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10
# print(type(n)) # <class 'int'>
print(n + 100) # 110
print(n.__add__(100)) # 110, , 내부적으로 add 메소드가 호출된 것
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))
print()

# 클래스 예제 1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {}, {}'.format(self._name, self._price)
    
    def __add__(self, x):
        print('called __add__')
        return self._price + x._price
    
    def __sub__(self, x):
        print('called __sub__')
        return self._price - x._price
    
    def __le__(self, x):
        print('called __le__')
        if self._price <= x._price:
            return True
        else:
            return False
        
    def __ge__(self, x):
        print('called __ge__')
        if self._price >= x._price:
            return True
        else:
            return False
        
# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 2500)
# s3 = Fruit('Apple', 10000)

# 일반적인 계산
# print(s1._price + s2._price)

# 매직 메소드
print(s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)
print(s2 - s1)
print(s1)
print(s2)