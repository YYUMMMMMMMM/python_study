# 중복 제거 : Remove Duplicates

'''
예제 1: 아래와 리스트에서 중복되는 원소를 제거 후 출력, 다양한 방법으로 코딩
x = ["a", 1, "b", 2, "a", 3, "b", 4, 5, "b"]
출력 결과 : [1, 2, 3, 4, 5, 'a', 'b']
'''

x = ["a", 1, "b", 2, "a", 3, "b", 4, 5, "b"]

print(f'출력 결과 : {list(set(x))}')

# Set(집합 자료형) : 중복 허용 하지 않음, 순서 없음
# List, Tuple : 순서 있음, 중복 허용
# OrderedDict : Dict 순서 보장 받을 수 있음(python 3.6 부터는 기본값), 많이 사용

# 방법 1
ex1 = list(set(x))
print(f'ex1 결과 : {ex1}')

# 방법 2 : 순서 유지 1
from collections import OrderedDict

ex2 = list(OrderedDict.fromkeys(x))
print(f'ex2 결과 : {ex2}')

# 방법 3 : 순서 유지 2
ex3 = []
for i in x:
    if i not in ex3:
        ex3.append(i)

print(f'ex3 결과 : {ex3}')

# 방법 4 : 리스트 컴프리헨션
ex4 = [i for idx, i in enumerate(x) if i not in x[:idx]]
print(f'ex4 결과 : {ex4}')

# # 리스트 컴프리헨션 기본 구조
# [expression for item in iterable if condition]
# expression: 조건을 만족하는 경우 사용할 값 (i).
# for item in iterable: x의 각 요소를 순회 (i는 현재 요소).
# if condition: 특정 조건이 참인 경우만 추가 (i not in x[:idx]).

# # 중복 제거 로직 : if i not in x[:idx]
# enumerate(x)는 인덱스 idx와 값 i를 제공
# x[:idx]는 현재 요소 i 이전까지의 리스트 슬라이스
# i not in x[:idx]는 i가 자신보다 앞에 이미 존재하는지 확인하는 조건
# 이 조건이 참이면 i를 결과 리스트에 추가
