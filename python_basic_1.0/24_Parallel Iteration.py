# 병렬 처리 : Parallel Iteration

'''
예제 1: 아래 3개의 리스트를 {key : a , value : b * c} 형태의 Dict(딕셔너리) 구조로 변경, 다양한 방법 활용
# 아래 조건 참조
a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]
출력 결과 : "{'one': 156.0, 'two': 148.0, 'three': 54.0, 'four': 315.0}"
'''

# 다양한 Iterable 그룹을 묶어 연산하는 과정은 중요
# zip : 다중 그룹의 반복가능한 자료형을 묶는 기능
# usage : zip(*iterables, strict=False) # Changed in version 3.10: Added the strict argument.
# python string package : https://www.oulub.com/en-US/Python/library.functions-zip

a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

# 방법 1
result1 = {}
for x, y, z in zip(a, b, c):
    result1[x] = y * z # key 값에 a를 넣고, value 값에 조건이었던 y * z를 넣음

print(f'ex1 결과 : {result1}')

# 방법 2 : 딕셔너리 컴프리헨션 사용
# print(f'ex1 결과 : {x: y * z for x, y, z in zip(a, b, c)}')
# ValueError: Invalid format specifier ' y * z for x, y, z in zip(a, b, c)' for object of type 'str'
# f"{...}" 안에서는 계산식을 바로 사용할 수 있지만, 복잡한 계산이나 반복문을 넣을 수는 없습니다.
# 이럴 때는 포매팅 외부에서 계산하고, 결과를 포매팅하는 방식으로 해결해야 합니다.
# 딕셔너리 컴프리헨션을 사용할 때는 f-string과 결합할 필요 없이 result 변수에 계산된 값을 담고, 그 값을 출력하는 방법을 사용해야 합니다.
result2 = {x: y * z for x, y, z in zip(a, b, c)}
print(f'ex2 결과 : {result2}')

# 방법 3 : 정적으로 dict 선언
print(f'ex3 결과 : {dict((x, y * z) for x, y, z in zip(a, b, c))}')