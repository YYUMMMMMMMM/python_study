# Dict 데이터 필터링 : Dictionary Data Filtering

'''
예제 1: 아래와 같은 딕셔너리 구조에서 Value 값이 25 이상 필터링 후 출력, 다양한 방법으로 코딩
d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}
출력 결과 : {'b': 33, 'd': 26, 'f': 120}
'''

d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}

# Dict 필터링 경우 : Key, value 둘다 필터링 가능
# Filter 함수도 사용
# Dict comprehension 으로 처리 가능
# { 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in dict }

# 방법 1
ex1 = {}
for k, v in d.items(): # .items() 튜플로 가져오기, 키와 밸류를 쌍으로 가져옴
    if v >= 25:
        ex1[k] = v
print(f'ex1 결과 : {ex1}')

# 방법 2 : Dict comprehension
ex2 = {k: v for k, v in d.items() if v >= 25}
print(f'ex2 결과 : {ex2}')

# 방법 3 : dict 선언하여 좀 더 명시적으로 작성
print(f'ex3 결과 : {dict((k, v) for k, v in d.items() if v >= 25)}')

# 방법 4 : filter, lambda 사용
ex4 = dict(filter(lambda v: v[1] >= 25, d.items()))
print(f'ex4 결과 : {ex4}')
