# Range 함수 활용 2 : More Range Technique

'''
예제 1: 아래와 같이 1부터 20까지 홀수 * 10, 짝수는 그대로 리스트로 출력
출력 결과 : [10, 2, 30, 4, 50, 6, 70, 8, 90, 10, 110, 12, 130, 14, 150, 16, 170, 18, 190, 20]
'''

result = []
for i in range(1, 21):
    if i % 2 == 1:
        result.append(i * 10)
    elif i % 2 == 0:
        result.append(i)

print(f'출력 결과 : {result}')

# result1 = [j for j in range(1, 21) if j % 2 == 1 j * 10 elif j % 2 == 0 j] # SyntaxError: invalid syntax
# 조건문에서 결과값이 누락됨 : 리스트 컴프리헨션의 if와 else 문법에서는 삼항 연산자 스타일로 작성해야 한다.
# elif 사용 불가 : 리스트 컴프리헨션에서 elif는 사용할 수 없다. if-else를 삼항 연산자로 표현해야 한다.
result1 = [j * 10 if j % 2 == 1 else j for j in range(1, 21)]
print(f'출력 결과 : {result1}')

# List Comprehension : 짧은 문법(Syntax)으로 간단하게 조건에 맞는 리스트 생성
# [x for x in list]
# [x for x in list if conditions]
# [ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in list]

# 방법 1
ex1 = []
for i in range(1, 21):
    if i % 2 != 0:
        ex1.append(i * 10)
    else:
        ex1.append(i)
print(f'ex1 결과 : {ex1}')

# 방법 2
ex2 = [x * 10 if x % 2 != 0 else x for x in range(1, 21)]
print(f'ex2 결과 : {ex2}')

print([[j for j in range(5)] for i in range(5)]) # 리스트 컴프리헨션 이해