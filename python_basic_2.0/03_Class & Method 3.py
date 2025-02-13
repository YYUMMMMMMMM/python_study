# Chapter02_03 클래스 & 메소드 심화
# 객체 지향 프로그래밍(OOP) > 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) > 함수 중심 > 데이터 방대 > 복잡
# 클래스 중심 > 데이터 중심 > 객체로 관리

class Car():
    """
    Car class
    Author : yyummmmmmmm
    Date : 2025.02.01
    Description : class, static, instance method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0
    # price_per_raise = 1.2

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # instance method : self 인자를 받는 메소드
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail info : {} {}'.format(self._company, self._details.get('price')))

    # instance method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    # instance method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    # class method : 첫번째 인자로 cls를 받음
    @classmethod
    def raise_price(cls, per):
        # cls.price_per_raise # Car.price_per_raise / Car = cls
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price inceased.')

    # static method : 인자를 필수로 받지 않음
    @staticmethod
    def is_benz(inst):
        if inst._company == 'Benz':
            return 'This car is {}'.format(inst._company)
        return 'This car is not Benz'



car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Benz', {'color' : 'Black', 'horsepower' : 300, 'price' : 7000})
car3 = Car('Kia', {'color' : 'Red', 'horsepower' : 100, 'price' : 2000})

# 전체 정보
car1.detail_info()
car2.detail_info()
print()

# 가격 정보 (직접 접근) 직접적으로 접근하는 방식은 좋지 않다.
# print(car1._details.get('price'))
# print(car2._details.get('price'))

# 가격 정보 (인상 전)
print(car1.get_price())
print(car2.get_price())
print()

# 가격 인상 (클래스 메소드 미사용, 직접 접근하는 방식은 좋지 않다.)
Car.price_per_raise = 1.4

# 가격 정보 (인상 후, 클래스 메소드 미사용)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 가격 인상 (클래스 메소드 사용)
Car.raise_price(1.6)

# 가격 정보 (인상 후, 클래스 메소드 사용)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 인스턴스 호출 (static method)
print(car1.is_benz(car1))
print(car2.is_benz(car2))
# 클래스 호출 (static method)
print(Car.is_benz(car1))
print(Car.is_benz(car2))