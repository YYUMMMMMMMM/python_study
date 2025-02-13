# 할당 및 비교 : Assigning & Comparison

'''
# 예제 1: 아래 파이썬 코드의 결과 값을 True or False 값을 예상
x = 15
y = 25
print(f'x == y : {x == y}')
print(f'x is y : {x is y}')
'''

# print(f'x value, id : {x}, {hex(id(x))}')
# print(f'y value, id : {y}, {hex(id(y))}')

'''
# 예제 2: 아래 파이썬 코드의 결과 값을 True or False 값을 예상
x = ['orange', 'banana', 'apple']
y = x

print(f'x == y : {x == y}')
print(f'x is y : {x is y}')
'''

# print(f'x value, id : {x}, {hex(id(x))}')
# print(f'y value, id : {y}, {hex(id(y))}')

'''
예제 3: 아래 파이썬 코드의 결과 값을 True or False 값을 예상
x = ['orange', 'banana', 'apple']
y = ['orange', 'banana', 'apple']

print(f'x == y : {x == y}')
print(f'x is y : {x is y}')
'''

# print(f'x value : {x}, x id : {hex(id(x))}')
# print(f'y value : {y}, y id : {hex(id(y))}') # 값은 같지만 메모리에 할당된 객체의 주소는 다르다.

# is , not is -> 참조, 객체(same object, 오브젝트)비교, 메모리에 할당된 객체의 주소를 비교
# == , != -> 값(value) 비교
# 값, 참조가 같은 비교는 is 사용(중요)