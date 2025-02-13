# Chapter05_04 일급함수(First-Class) - 데코레이터(Decorator)
# 데코레이터를 이해하기 위해 선행되어야하는 내용
# 1. 클로저
# 2. 함수를 일급 인자(first-class argument)로 활용하는 법
# 3. 가변 인자
# 4. 인자 풀기(argument unpacking)
# 5. 파이썬이 소스코드를 불러오는 자세한 과정

# 데코레이터(Decorator) 사용 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크를 할 수 있는 공통 기능
# 3. 조합해서 사용 용이

# 데코레이터(Decorator) 사용 단점
# 1. 가독성 감소?, 코드를 작성하기 나름이다.
# 2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리할 수 있다.
# 3. 디버깅 불편

# 클로저와 데코레이터 관계를 이해해야한다.
# 실습 1
import time

# 클로저 패턴으로 작성
def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행 (핵심)
        result = func(*args) # 부모에서 넘어온 인자가 실행되기 때문에 자유변수로써 값을 받아 저장할 수 있다.
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

# # 데코레이터 미사용
# def time_func(seconds):
#     time.sleep(seconds)

# def sum_func(*numbers):
#     return sum(numbers)

# none_deco1 = perf_clock(time_func)
# none_deco2 = perf_clock(sum_func)
# print(none_deco1, none_deco1.__code__.co_freevars)
# print(none_deco2, none_deco2.__code__.co_freevars)

# print('-' * 40, 'Called None Decorator -> time_func')
# print()
# none_deco1(1.5) # [1.50049s] time_func(1.5) -> None
# print('-' * 40, 'Called None Decorator -> sum_func')
# print()
# none_deco2(100, 200, 300, 400, 500) # [0.00112s] sum_func(100, 200, 300, 400, 500) -> 1500

# 데코레이터 사용
@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

print('-' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5) # 함수 자체를 실행해주면 된다. [1.50027s] time_func(1.5) -> None
print('-' * 40, 'Called Decorator -> sum_func')
print()
sum_func(100, 200, 300, 400, 500) # [0.00007s] sum_func(100, 200, 300, 400, 500) -> 1500





# 실습 2