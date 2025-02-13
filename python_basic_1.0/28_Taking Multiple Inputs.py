# 사용자 입력 처리 : Taking Multiple Inputs

'''
예제 1: 사용자에게 정수를 3회 입력 받은 후 평균 값을 출력,다양한 방법으로 시도

# 아래 조건 참조
x = 사용자 입력 -> 15
y = 사용자 입력 -> 25
z = 사용자 입력 -> 45

# 출력
28.3333333333 # (15 + 25 + 45) / 3
'''

# x = int(input("입력 : "))
# y = int(input("입력 : "))
# z = int(input("입력 : "))

# total = x + y + z
# avg = total / 3
# print(f'출력 : {avg}')

# for i in range(0, num):
#     i = input("사용자 입력 : ")
#     total += int(i)
#     avg = total / num
# print(f'평균값 : {avg}')

input_data = int(input("입력 횟수 : "))
num = int(input_data)
total = 0

def input_avg():
    total = 0
    for i in range(0, num):
        i = input("사용자 입력 : ")
        total += int(i)
        avg = round(total / num, 10)
    return avg
print(f'평균값 : {input_avg()}')

# Input 함수는 기본 입력 타입은 Str 자료형인 부분을 꼭 기억, 타입 캐스팅 필요
# 연속적으로 편하게 입력받을 수 있는 방법을 생각
# 평균, 합계는 리스트로 변환해서 계산하면 매우 편하다.
# 참고 : https://docs.python.org/3/library/functions.html#input

# 방법 1
# x = int(input("Enter first value: "))
# y = int(input("Enter second value: "))
# z = int(input("Enter third value: "))

# print((x + y + z) / 3) # 총 개수를 카운트 해야함
# print()

# 방법 2 : split() 활용
# x, y, z = input("Enter three value: ").split()
# print((int(x) + int(y) + int(z) /3)

# 방법 3
# l = list(map(int, input("Enter three value: ").split()))
# print(round(sum(l) / len(l), 2))
