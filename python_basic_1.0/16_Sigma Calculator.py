# 계산 문제 : Sigma Calculator

'''
예제 1: N까지 합(Sigma)을 구하는 공식을 함수 형태로 작성 후 출력, 다양한 방법 사용
입력 : 10 
출력 결과 : 55
'''

num = int(input('입력 : '))
result = 0
for i in range(1, num + 1):
    result += i
print(f'출력 결과 : {result}')

# 파이썬 언어 활용 분야인 데이터 사이언스 분야에서 다양한 방정식(공식) 구현 필요성
# 제공되지 않는 수학 공식을 코드로 표현하는 능력 중요
# 참조 : https://www.mathsisfun.com/numbers/sigma-calculator.html

# 방법 1
# n = input('입력 : ')
# def sigma_sum1(n):
#     tot = 0
#     for i in range(1, n + 1):
#         tot = tot + i
#     return tot
# print(f'ex1 결과 : {sigma_sum1(int(n))}')

# 방법 2
# n = input('입력 : ')
# def sigma_sum2(n):
#     return n * (n + 1) // 2
# print(f'ex2 결과 : {sigma_sum2(int(n))}')

# 방법 3
n = input('입력 : ')
def sigma_sum3(n):
    return sum(range(n + 1))
print(f'ex3 결과 : {sigma_sum3(int(n))}')