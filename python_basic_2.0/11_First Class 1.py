# Chapter05_01 일급함수(First-Class) - 기본 특징
# 함수형 프로그래밍의 특징 정리해보기
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 함수를 변수로 할당 가능
# 3. 함수를 다른 함수의 인수(parameter)로 전달 가능
# 4. 함수를 함수의 결과값으로 반환(return) 가능

# 함수 객체
def factorial(n):
    '''Factorial Function > n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1) # 재귀함수, 함수 내에서 함수를 다시 호출

class A:
    pass

# 증명
print(factorial(5)) # 120
print(factorial.__doc__)
print(type(factorial), type(A))
print(dir(factorial)) # 함수이지만 객체 취급을 받는다.
print(set(sorted(dir(factorial)))- set(sorted(dir(A)))) # 함수만 가지고 있는 속성들만 뽑기
# {'__kwdefaults__', '__name__', '__call__', '__globals__', '__code__', '__builtins__', '__defaults__', '__get__', '__type_params__', '__qualname__', '__closure__', '__annotations__'}
print(factorial.__name__)
print(factorial.__code__)

# 변수에 할당 가능한 지 증명
var_func = factorial
print(var_func) # <function factorial at 0x000001F70E2FFA60>
print(var_func(10)) # 3628800
print(list(map(var_func, range(1, 11)))) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# 함수를 다른 함수 인수 전달 및 함수로 결과 반환 증명 -> 고위 함수(Higher-order function)
# map, filter, reduce
print(list(map(var_func, filter(lambda x : x % 2, range(1, 6))))) # var_func 함수를 map() 함수의 인자로 전달, lambda(익명함수) 역시 filter() 함수의 인자로 전달됨
print([var_func(i) for i in range(1, 6) if i % 2]) # 홀수 팩토리얼만 출력
print()

# reduce
from functools import reduce
from operator import add

print(sum(range(1, 11)))
print(reduce(add, range(1, 11)))

# 익명함수(Lambda)
# 가급적 주석 작성
# 가급적 익명함수보다 일반함수를 작성
# 익명함수형태라면 일반 함수 형태로 리팩토링을 권장
print(reduce(lambda x, t : x + t, range(1, 11)))
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한 지 확인
# 호출 가능 확인
print(callable(str), callable(A), callable(list), callable(var_func), callable(factorial), callable(3.14)) # True True True True True False
# callable(3.14) 상수 자체로는 함수 형태로 호출이 불가능

# Partial 사용법 : 중요! 인수를 고정 -> 주로 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5) # 5 * ?, 함수를 인자로 전달 가능하고 함수를 변수에 할당
print(five(10))
print(five(100))

# 고정 추가
six = partial(five, 6)
print(six())
# print(six(10)) # TypeError: mul expected 2 arguments, got 3
print([five(i) for i in range(1, 10)])
print(list(map(five, range(1, 10))))