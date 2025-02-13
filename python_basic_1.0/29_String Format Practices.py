# 문자열 포맷팅 : String Format Practices

'''
예제 1: 아래 String 포맷 출력문에서 결과 값이 다른 것은 무엇?

# 공통 변수 선언
x = 10
y = 20
serialno = 308276567
n = 'Kim'

# 출력1
ex1 = 'n = %s, s = %x, sum=%d' % (n, serialno, (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {serialno}, sum={sum}'.format(n=n, serialno=serialno, sum=x + y)
print(ex2)

# 출력3
ex3 = f'n = {n}, s = {serialno}, sum={x + y}'
print(ex3)
'''

# 파이썬 문자 출력(서식)은 여러가지 방법이 있다.
# 1. % Operator(Old Style) : 가급적 사용 안하는 것을 권장
# 2. str.format(New Style) : 사용 권장
# 3. f-Strings (Python 3.6+) : 사용 권장
# 4. Template String(from string import Template)
# 참고 : https://docs.python.org/3/library/string.html#template-strings
# 참고 : https://realpython.com/python-f-strings/

# 공통 변수 선언
x = 10
y = 20
serialno = 308276567
n = 'Kim'

# 출력 1 : % Operator(Old Style)
ex1 = 'n = %s, s = %x, sum=%d' % (n, serialno, (x + y)) # %s : 문자열로 출력, %x : 16진수로 출력, %d : 그대로 출력
print(ex1)


# 출력 2 : str.format(New Style), {} 사용,
ex2 = 'n = {n}, s = {serialno}, sum={sum}'.format(n=n, serialno=serialno, sum=x + y)
print(ex2)


# 출력 3 : f-Strings (Python 3.6+)
ex3 = f'n = {n}, s = {serialno}, sum={x + y}' # 선언된 변수를 {}으로 그대로 사용 가능
print(ex3)

# 출력 4 : Template String(from string import Template)
from string import Template
ex4 = 'n = $n, s = $serialno, sum = $sum' # 변수에 템플릿을 담아 둠
t = Template(ex4)
t.substitute(n = n, serialno = serialno, sum = x + y)

# 출력 5 : 다양한 f-String 연습
# 진수
# (2진수 : b, 8진수 : o, 16진수 : x|X)

k = 77
print(f"k 2: {k:b}, k 8: {k:o}")
print(f"k 16: {k:x}, k 16: {k:X}")
print()

# 구분 기호
m = 1000000000

print(f'm: {m:,}')
print()

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽
g = 20
print(f'g:{g:10}')
print(f'g center: {g:^10}.')
print(f'g left: {g:<10}.')
print(f'g right: {g:>10}.')
print()

# 채우기
print(f'g center: {g:-^10}.')
print(f'g center: {g:*^10}.')