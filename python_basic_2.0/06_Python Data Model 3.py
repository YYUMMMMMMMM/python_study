# Chapter03_03 파이썬 데이터 모델 추상화
# special method(magic method)
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(functions), 클래스(class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 두 점 사이의 거리 공식 예제
# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)
# print(pt3.x)
# print(pt4[1])
l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2) # 인덱스로도 접근 가능
print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = False 예약어 사용했을 때 rename=True로 해주면 에러 해결됨

# 출력
print(Point1, Point2, Point3, Point4) # <class '__main__.Point'>
print()

# Dict to Unpacking
temp_dict = {'x' : 75, 'y' : 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=80)
p4 = Point4(10, 20, 40, 60) # rename test
p5 = Point3(**temp_dict)

print(p1)
print(p2)
print(p3)
print(p4) #  중복된 키값과 예약어는 자동으로 난수로 키값을 생성해준다.
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# Unpacking
x, y = p3
print(x, y)

# 네임드 튜플 메소드
temp = [52, 49]

# _make() : 리스트를 네임드 튜플로 변환하여 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fields() : 필드 네임 확인, 딕셔너리에서 키값만 조회할 때 사용
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 정렬된 딕셔너리를 반환,  (Python 3.8 이상에서는 일반 dict 반환)
print(p1._asdict())
print(p4._asdict())

from collections import OrderedDict
# _asdict() 결과를 OrderedDict로 변환
print(OrderedDict(p1._asdict()))
print(OrderedDict(p4._asdict()))

# 실 사용 실습
# 한 반에 20명, 4개 반이 있다고 가정 (A, B, C, D), B14, D18 학생

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# 추천 (가독성)
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1, 21)]]
print(len(students2))
print(students2)

# 출력
for s in students2:
    print(s)