# 지역 변수 : Local Variables

'''
예제 1: 아래 함수 실행 후 step1, step2, step3 결과를 예측

a = 20

def test():
    # 지역변수
    a = 35
    return a

print('step1 : ', a)

a = 100

print('step2 : ', a)
print('step3 : ', test())
'''

a = 20

def test():
    # 지역변수
    a = 35
    return a

print('step1 : ', a) # 20

a = 100

print('step2 : ', a) # 100
print('step3 : ', test()) # 35

# 예제 2
a = 20

def test():
    global a

    # 출력 값 이해 필요 (중요)
    print(f'ex3 결과 : {a}') # 20, X (100) 아래에서 test() 함수를 호출했을 때 재할당된 전역변수 100으로 출력되는 것

    a = 35
    return a

print(f'ex1 결과 : {a}') # 20, O 전역변수 20 출력

a = 100
print(f'ex2 결과 : {a}') # 100, O 재할당된 전역변수 100 출력
print(f'ex4 결과 : {test()}') # 35, O test() 함수의 리턴값 35 출력

# 출력 값 이해 필요 (중요)
print(f'ex5 결과 : {a}') # 100, X 위에서 test() 함수를 호출했음으로 리턴값 35 출력

a = 7777
print(f'ex6 결과 : {a}') # 7777