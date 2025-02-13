"""
Chapter 03
Python Advanced(3) - Descriptor 1
Keyword - descriptor, get, set, del, property

"""
"""
디스크립터
1. 객체에서 서로 다른 객체를 속성값으로 가지는 것
2. read, write, delete 등을 미리 정의 가능
3. data descriptor(set, del), non-data descriptor(get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능

"""

# 예제 1 : 기본적인 descriptor
class DescriptorEx1:
    def __init__(self, name='Default'):
        self.name = name
        
    def __get__(self, obj, objtype):
        return 'Get method called > self : {}, obj : {}, objtype : {}, name : {}'.format(self, obj, objtype, self.name)
    
    def __set__(self, obj, name):
        print('Set method called.')
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name should be string.')
        
    def __delete__(self, obj):
        print('Delete method called.')
        self.name = None

class Sample1:
    name = DescriptorEx1() # DescriptorEx1 함수 내부의 메소드가 알아서 호출된다.
                            # property 클래스와 사용 클래스가 별도
s1 = Sample1()


# __set__ 호출
s1.name = 'Descriptor Test 1' # Set method called.

# 예외 발생
# s1.name = 10 # TypeError: Name should be string.

# attr 확인
# __get__ 호출
print('Ex1 > ', s1.name) # name : Descriptor Test 1

# __delete__ 호출
del s1.name

# 삭제 확인
# __get__ 호출
print('Ex1 > ', s1.name) # name : None


# 예제 2 : property 클래스 사용하여 descriptor 직접 구현
# class property(fget=None, fset=None, fdel=None, doc=None)

class DescriptorEx2(object):
    def __init__(self, value):
        self._name = value
    
    def getVal(self): # 메소드 네이밍이 자유롭다
        return 'Get method called. > self : {}, name : {}'.format(self, self._name)
    
    def setVal(self, value):
        print('Set method called.')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Name should be string.')
        
    def delVal(self):
        print('Delete method called.')
        self._name = None
    name = property(getVal, setVal, delVal, 'Property Method Example')
# property 클래스와 사용 클래스가 동일하게 하나로되는 대신 프로퍼티로 호출하여 사용

s2 = DescriptorEx2('Descriptor Test 2') # 초기값

# getVal 호출
print('Ex2 > ', s2.name) # name : Descriptor Test 2

# setVal 호출
s2.name = 'Descriptor'

# 예외 발생
# s2.name = 100 # TypeError: Name should be string.
print('Ex2 > ', s2.name) # name : Descriptor

# delVal 호출
del s2.name
print('Ex2 > ', s2.name) # name : None

# doc 확인
print('Ex2 > ', DescriptorEx2.name.__doc__) # Property Method Example
