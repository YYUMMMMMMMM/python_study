"""
Chapter 01
Python Advanced(1) - Lambda, Reduce, Map, Filter Functions
Keyword - lambda, reduce, map, filter

"""
"""
lambda 장점 : 익명, 힙(Heep) 영역에서 사용 즉시 소멸 (메모리 절약), pythonic?, 파이썬 가비지 컬렉션(Count=0)
일반함수 : 재사용성을 위해서 메모리에 저장
시퀀스형 전처리에 Reduce, Map, Filter를 주로 사용
map(), filter(), reduce() : 2개의 인자를 받음 (함수, 시퀀스형 데이터)

"""

# 예제 1 : lambda
# def test(a, b, c):
#     return a + b + c

cul = lambda a, b, c : a + b + c
print('Ex1 > ', cul(10, 15, 20))

# 예제 2 : map() : 두 개의 args를 받음
digits1 = [x * 10 for x in range(1, 11)]
print('Ex2 > ', digits1)

# def ex2_func(x): # 메모리에 저장되기 때문에 lambda 사용이 권장된다.
#     return x ** 2
# result = list(map(ex2_func, digits1))

result = list(map(lambda i : i ** 2, digits1))
print('Ex2 > ', result)

def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)

print('Ex2 > ', list(also_square(digits1)))

# 예제 3 : filter()
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 만약에 1억개의 데이터가 있다고 가정
result = list(filter(lambda x : x % 2 == 0, digits2))
print('Ex3 > ', result)

def also_evens(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)
print('Ex3 > ', list(also_evens(digits2)))

# 예제 4 : reduce() : 시퀀스형 데이터를 누적하여 반환, 문자열도 가능
from functools import reduce

digits3 = [x for x in range(1, 101)]

result = reduce(lambda x, y : x + y, digits3)
print('Ex4 > ', result)

def also_add(nums):
    def add_plus(x, y):
        return x + y
    return reduce(add_plus, nums)
print('Ex4 > ', also_add(digits3))
