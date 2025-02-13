"""
Chapter 03
Python Advanced(3) - Meta Class 3
Keyword - type inheritance, custom metaclass

"""
"""
메타클래스 상속
1. type클래스를 상속한다는 뜻
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
    - 클래스 생성 가로채기(intercept)
    - 클래스 수정하기(modifiy)
    - 클래스 개선(기능추가)
    - 수정된 클래스 반환

"""

# 예제 1 : 커스텀 메타클래스 생성 (type 클래스 상속 X)
def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new
# 클래스 외부에 메소드를 빼놓으면 컴포넌트 형식으로 어디에서든지 조립 가능하다.

# list 클래스를 상속, 위 메소드를 2개 추가
CustomList1 = type('CustomList1',
                   (list,),
                   {'desc' : '커스텀 리스트', 'cus_mul' : cus_mul, 'cus_replace' : cus_replace}
                   )

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9]) # (self), self에 초기화값을 넣어줌
c1.cus_mul(1000) # (d)
c1.cus_replace(1000, 7777) # (old, new)
print('Ex1 > ', c1)
print('Ex1 > ', c1.desc)
print('Ex1 > ', dir(c1))

# 예제 2 : 커스텀 메타클래스 생성 (type 클래스 상속 O)
# class MetaClassName(type):
#     def __new__(metacls, name, bases, namespace):
        # 코드 작성
        
# 실행 순서 : new > init > call 순서
class CustomListMeta(type):
    # init : 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print('__init__ > ', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)
        
    # call : 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print('__call__ > ', self, *args, **kwargs)
        return super().__call__(*args, **kwargs)
        # instance = super().__call__(*args, **kwargs)
        # return instance
        # AttributeError: 'NoneType' object has no attribute 'cus_mul'
        # __call__ 메서드는 인스턴스를 리턴해줘야한다.
        
    # new : 클래스 인스턴스 생성(메모리 초기화(메모리에 할당 됨))
    def __new__(metacls, name, bases, namespace):
        print('__new__ > ', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀 리스트2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace
        return type.__new__(metacls, name, bases, namespace)
        # new는 반드시 return이 있어야 함
        
CustomList2 = CustomListMeta('CustomList2',
                             (list, ),
                             {}
                            )
c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2.cus_mul(1000)
c2.cus_replace(1000, 8888)
print('Ex2 > ', c2)
print('Ex2 > ', c2.desc)

# 상속 확인
print(CustomList2.__mro__)