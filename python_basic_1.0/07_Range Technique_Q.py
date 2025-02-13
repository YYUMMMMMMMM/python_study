# Range 함수 활용 1 : Range Technique

'''
예제 1: 다음과 같이 30 ~ -10까지 -2씩 감소한 결과를 리스트로 출력
출력 결과 : [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10]
'''
result = []
for i in range(30, -11, -2):
    result.append(i)
print(f'출력 결과 : {result}')

# range 함수(내장) : 주어진 범위 사이의 숫자형 시퀀스 반환
# loop 관점에서 핵심적인 함수(주로 for, while 함께 사용)
# range(stop) takes one argument.
# range(start, stop) takes two arguments.
# range(start, stop, step) takes three arguments.

# 방법 1
ex1 = []
for i in range(30, -12, -2):
    ex1.append(i)
print(f'방법 1 출력 결과 : {ex1}')

# 방법 2
ex2 = list(range(30, -12, -2))
print(f'방법 2 출력 결과 : {ex2}')