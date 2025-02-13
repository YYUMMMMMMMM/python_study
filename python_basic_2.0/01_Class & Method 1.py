# Chapter02_01 클래스 & 메소드 심화
# 객체 지향 프로그래밍(OOP) > 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) > 함수 중심 > 데이터 방대 > 복잡
# 클래스 중심 > 데이터 중심 > 객체로 관리

# 일반적인 코딩
# 차량 1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower' : 400},
    {'price' : 8000},
]

# 차량 2
car_company_2 = 'Benz'
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower' : 300},
    {'price' : 7000},
]

# 차량 3
car_company_3 = 'Kia'
car_detail_3 = [
    {'color' : 'Red'},
    {'horsepower' : 100},
    {'price' : 2000},
]


# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성 존재, 삭제가 불편
# 데이터의 양이 매우 많을 때는 인덱스 번호를 알기가 쉽지 않다.
car_company_list = ['Ferrari', 'Benz', 'Kia']
car_detail_list = [
    {'color' : 'White', 'horsepower' : 400, 'price' : 8000},
    {'color' : 'Black', 'horsepower' : 300, 'price' : 7000},
    {'color' : 'Red', 'horsepower' : 100, 'price' : 2000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등
car_dicts = [
    {'car_company' : 'Ferrari', 'car_detail' : {'color' : 'White', 'horsepower' : 400, 'price' : 8000}},
    {'car_company' : 'Benz', 'car_detail' : {'color' : 'Black', 'horsepower' : 300, 'price' : 7000}},
    {'car_company' : 'Kia', 'car_detail' : {'color' : 'Red', 'horsepower' : 100, 'price' : 2000}},
]

# pop(key, 'default')
del car_dicts[1]
print(car_dicts)

print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): # 사용자 레벨
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 개발자 레벨, 객체정보까지 표시해줌
        return 'repr : {} - {}'.format(self._company, self._details)
    
    # str, repr 차이점 정리

    def __reduce__(self):
        pass

car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Benz', {'color' : 'Black', 'horsepower' : 300, 'price' : 7000})
car3 = Car('Kia', {'color' : 'Red', 'horsepower' : 100, 'price' : 2000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# print(dir(car1))
# print(dir(car2))
# print(dir(car3))

print()

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)
print(car_list)

print()

# 반복(__str__)
for x in car_list:
    # print(x)
    print(repr(x)) # repr은 명시적으로 선언해주어야 함