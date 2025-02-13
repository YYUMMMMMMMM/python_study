# Dict 아이템 추가 : Add Dict Items

'''
예제 1: 아래와 같이 Dictionary에 {'c': 'banana', 'd': 'kiwi'}를 추가, 가능한 방법 모두 구현
d = {'a': 'apple', 'b': 'grape'}
출력 결과 : {'a': 'apple', 'b': 'grape', 'c': 'banana', 'd': 'kiwi'}
'''

d = {'a': 'apple', 'b': 'grape'}
d['c'] = 'banana'
d['d'] = 'kiwi'

print(f'출력 결과 : {d}')

# 기존 Dict 구조에 새로운 item 추가, 제거는 자주 일어난다.
# Python Dict에서 Key로 요소의 값에 접근할 수 있다. -> e[key]
# Dict의 update 함수도 사용

# 방법 1
e = {'a': 'apple', 'b': 'grape'}

# e.update({'c': 'banana', 'd': 'kiwi'}) 
e.update({'a': 'banana', 'b': 'kiwi'}) # d.update 하면 overwrite
print(f'ex1 결과 : {e}')