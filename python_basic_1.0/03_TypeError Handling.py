# 에러 핸들링 : TypeError Handling

'''
# 예제1 : 아래 파이썬 코드가 왜 에러(예외)가 발생하는지 생각해보고 동작하도록 수정 후 작성
# x = "Seoul"
# y = 25
# z = x + y
'''

x = "Seoul"
y = 25
# z = x + y
z = x + str(y) # 문자열 <-> 정수 연산은 형변환(Type Casting)이 필요

# print(f'x + y : {z}')
# TypeError: can only concatenate str (not "int") to str, 문자열과 숫자를 더했기 때문에 에러가 발생한다.

print(f'x + y : {z}')

# TypeError Handling 추가 학습
# Calling a non-callable 인 경우
# etc = "Korea Seoul"
# print(etc()) # TypeError: 'str' object is not callable, 문자열을 함수형으로 호출했을 때 발생하는 에러

# 리스트 인덱스 타입 에러인 경우
c = [1, 2, 3, 4, 5]
# print(c["2"]) # TypeError: list indices must be integers or slices, not str, 리스트의 원소에 접근할 때는 int, slice 형태로 넣어줘야 함
print(c[3])
print(c[1:3])