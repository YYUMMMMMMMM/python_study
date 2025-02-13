# 비밀번호 체크 : Password Checker

'''
예제 1: 아래 조건과 같이 사용자 입력 문자열(비밀번호)를 체크, while, input 사용
# 사용자 비밀번호 입력
# 조건1 : 비밀번호는 반드시 8자 이상이어야 합니다.
# 조건2 : 반드시 1개 이상의 대문자는 포함되어 있어야 합니다.
# 조건3 : 반드시 1개 이상의 숫자를 포함해야 합니다.

# 사용자 입력1
password1 = input() # a1234!! 

# 출력 결과1
# 8자 이하, 대문자 미포함
비밀번호 조건이 맞지 않습니다.

# 사용자 입력2
password2 = input() # A777abcd!

# 출력 결과2
비밀번호 형식이 맞습니다.
'''

# 주어진 문자열에 대해 조건을 체크하는 문제 해결 능력
# 정규표현식도 사용 가능

# while 문을 활용해서 프로그램 흐름이 끊기지 않게 작성
    
# any 함수 : 한 개라도 참(True)일 경우 True 반환(일부 만족)
# print(any([True, True, True]))
# print(any([True, True, False]))
# print(any([False, False, False]))

# all 함수 : 전체가 참(True)일 경우 True 반환(모두 만족)
# print(all([True, True, True]))
# print(all([True, True, False]))

# 내부 문자열 함수 isdigit(), isupper() 함수 등을 활용
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# 방법 1
while True:
    results = []
    password = input("비밀번호 입력 : ")
    print()
    if not any(i.isdigit() for i in password): # isdigit() : 최소 1개 이상의 숫자가 포함되어있는지 확인
        results.append("최소 1개 이상의 숫자가 포함되어야 합니다.")
    if not any(i.isupper() for i in password): # isdigit() : 최소 1개 이상의 대문자가 포함되어있는지 확인
        results.append("최소 1개 이상의 대문자가 포함되어야 합니다.")
    if len(password) < 8:
        results.append("비밀번호는 최소 8자 이상입니다.")
    if len(results) == 0:
        print("비밀번호 형식이 맞습니다.")
        break
    else:
        print("아래와 같이 비밀번호 조건이 맞지 않습니다.")
        for txt in results:
            print("-->", txt)
    