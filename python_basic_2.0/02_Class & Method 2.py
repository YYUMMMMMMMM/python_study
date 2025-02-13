# Chapter02_02 클래스 & 메소드 심화
# 객체 지향 프로그래밍(OOP) > 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) > 함수 중심 > 데이터 방대 > 복잡
# 클래스 중심 > 데이터 중심 > 객체로 관리

class Car():
    """
    Car class
    Author : yyummmmmmmm
    Date : 2025.02.01
    사용법 : ~
    """
    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self.car_count = 10
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail info : {} {}'.format(self._company, self._details.get('price')))

# self 의미 : 클래스를 기반으로 생성된 인스턴스의 고유값(ID)을 할당해줌
car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Benz', {'color' : 'Black', 'horsepower' : 300, 'price' : 7000})
car3 = Car('Kia', {'color' : 'Red', 'horsepower' : 100, 'price' : 2000})

# ID 확인
print(id(car1))
print(id(car2))
print(car1._company == car2._company)
print(car1 is car2)
print()

# dir & __dict__ 확인
print(dir(car1)) # 값이 나오지 않음
print(car1.__dict__) # 키와 밸류값을 보여줌
print()

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()
Car.detail_info(car2) # 클래스 이름으로 바로 접근 시 self 인자를 전달해주어야 함
# 에러
# Car.detail_info() # TypeError: Car.detail_info() missing 1 required positional argument: 'self'
print()

# 비교
print(car1.__class__,car2.__class__)
print(id(car1.__class__), id(car2.__class__)) # 클래스 자체의 ID값을 출력했기때문에 같은 값이 나옴
print(id(car1.__class__) == id(car2.__class__))
print()

# 공유 확인
print(car1.car_count) # 클래스 변수는 클래스로 생성된 인스턴스의 갯수를 모두 공유한다.
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1)) # 클래스 변수까지 나옴
print()

# 접근
print(car1.car_count)
print(Car.car_count) # 정석적인 방법
print()

# 삭제
del car2
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 없다면 > 상위(클래스 변수, 부모 클래스 변수))