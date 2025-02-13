# 시퀀스 타입 인덱싱 : Sequence Type Indexing

'''
예제 1: 아래 리스트(List)에서 index 함수를 포함한 다양한 방법으로 "Banana"를 인덱싱(추출) 해보세요.
x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana', 'Strawberry']
출력 결과 : Banana
'''

x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana', 'Strawberry']
print(f'출력 결과 : {x[4]}')
print(f'출력 결과 : {x[-2]}')

# 시퀀스 자료형(데이터의 값이 연속적으로 이루어진 자료구조) : List, Tuple, Str, Range..
# List 관련 함수는 중요!
# cmp, len, max, min, list, append, count, extend, index, insert, pop, remove, reverse, sort..
# index 함수 대소문자 구분
# sort, sorted 함수 차이도 중요


# 다양한 방법
print(f'출력 결과 : {x.index("Banana")}')
print(f'출력 결과 : {x[x.index("Banana")]}')
print(f'데이터의 포함 여부 확인 : {"Banana" in x}') # index 함수 사용 전 데이터 포함 여부 확인
print(f'출력 결과 : {x[x.index("Banana", 0, len(x))]}')
print(f'출력 결과 : {x[x.index("Banana", 4, len(x))]}')
# print(f'출력 결과 : {x[x.index("Banana", 5, len(x))]}') ValueError: 'Banana' is not in list, x[x.index("찾고자하는 데이터", 시작 인덱스, 끝 인덱스)]