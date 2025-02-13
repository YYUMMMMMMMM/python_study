# Dict 합 구하기 : Dict Items Sum

'''
예제 1: 아래와 같은 Dict 구조에서 모든 value 값의 합(Sum)을 가능한 모든 방법 코딩 
d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}
출력결과 : 2327
'''

d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}

result = 0
for data in d:
    # print(data) # key
    # print(d[data]) # value
    result += d[data]
print(f'출력 결과 : {result}')

# Dict : Key와 value의 대응관계를 갖는 자료형(해시테이블, 가변적-수정가능)
# 자주 사용하는 함수 : get(), values(), keys() 
# 다양한 Dict 선언 방법에 대해서 알아두어야 한다.

# 빈 딕셔너리
# d = {}

# 자주 사용
# d = {1: 'banana', 2: 'apple'}

# 다양한 키 조합
# d = {'name': 'Lee', 1: [5, 6, 7]}

# 직접 선언
# d = dict({1:'banana', 2:'apple'})

# 시퀀스형 페어로 선언
# d = dict([(1,'banana'), (2,'apple')])

# 방법 1
# print(d.values())
total = 0
for i in d.values():
    total += i
print(f'ex1 결과 : {total}')

# 방법 2
# TypeError: 'int' object is not callable 위 코드에서 sum을 변수 이름으로 재정의하여 에러 떨어짐
# del sum   # 변수 삭제, 내장 함수로 복구
print(f'ex2 결과 : {sum(d.values())}')

# 방법 3
print(f'ex2 결과 : {sum([d[item] for item in d])}')

# 방법 4 : reduce
from functools import reduce
print(f'ex4 결과 : {reduce(lambda x,y:x+y,d.values())}')