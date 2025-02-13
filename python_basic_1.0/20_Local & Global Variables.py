# 지역 & 전역 변수 : Local & Global Variables

'''
예제 1: 아래 함수 실행 후 Step1, Step2 -> a, b, x, y 결과를 예측

def test(x, y):
    global a
    a = 49
    x,y = y,x
    b = 53
    b = 7
    c = 135
    # 예상1
    print('Step1 : ', a, b, x, y)

a, b, x, y = 8, 13, 33,44 

# 함수 실행
test(23, 7)

# 예상 2
print('Step2 : ', a, b, x, y)
'''

def test(x, y):
    global a
    a = 49
    x,y = y,x
    # global b
    b = 53
    b = 7
    a = 135
    # 예상1
    print('Step1 : ', a, b, x, y) # 135 7 7 23, O

a, b, x, y = 8, 13, 33, 44 

# 함수 실행
test(23, 7)

# 예상 2
print('Step2 : ', a, b, x, y) # 8 13 33 44, X (135 13 33 44)
# a의 경우 위에서 test() 함수가 호출되었기 때문에 글로벌 키워드로 선언된 a의 재할당된 값이 출력되는 것 같다.
# b도 글로벌 키워드로 선언해보자. 135 7 33 44가 출력될 것