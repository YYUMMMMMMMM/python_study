# 시퀀스 타입 조회 : Sequence Item Selection

'''
예제 1: 아래 리스트(List)에서 apple, kiwi를 추출해서 대문자 리스트로 출력, 가능한 다양한 방법으로 코딩
x = ["grapes", "mango", "orange", "peach", "apple", "lime", "banana", "cherry", "tomato", "kiwi", "blueberry", "watermelon"]
출력 결과 : [APPLE, KIWI]
'''

x = ["grapes", "mango", "orange", "peach", "apple", "lime", "banana", "cherry", "tomato", "kiwi", "blueberry", "watermelon"]

result = []

for i in x:
    if (i == "apple"):
        result += [i]
        continue
    elif (i == "kiwi"):
        result += [i]
        break
# print(f'출력 결과 : {result.upper()}')
# upper() 메서드가 문자열에만 사용 가능하다. 현재 result는 리스트이고, 리스트에는 upper() 메서드가 없다.

# 리스트의 요소를 대문자로 변환하여 출력
# print(f'출력 결과 : {[item.upper() for item in result]}')

# 파이썬에서 사용가능한 반복문(for, while) -> (break, continue) 필수 기억!
# 시퀀스 자료형(데이터의 값이 연속적으로 이루어진 자료구조) : List, Tuple, Str, Range..
# filter(f, iterable) 함수는 정말 많이 사용 (map 함수도 중요!) * 매우 중요!!
# lambda expression(형식)은 다른 함수의 인수 전달 형태로 사용

# 방법 1
ex1 = []
for i in range(len(x)):
    if x[i] == 'apple' or x[i] == 'kiwi':
        ex1.append(x[i].upper())

print(f'방법 1 출력 결과 : {ex1}')

# 방법 2
ex2 = list(map(lambda b: b.upper(), filter(lambda a: a == 'apple' or a == 'kiwi', x))) # filter와 lambda 형식 사용
print(f'방법 2 출력 결과 : {ex2}')

# 방법 3
ex3 = [a.upper() for a in x if a == 'apple' or a == 'kiwi'] # 리스트 컴프리헨션 사용
print(f'방법 3 출력 결과 : {ex3}')