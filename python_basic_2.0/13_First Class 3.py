# Chapter05_03 일급함수(First-Class) - 클로저(Closure) 심화
# 외부에서 호출된 함수의 변수값 또는 상태(레퍼런스)를 복사 후에 저장하고 나중에 접근(엑세스) 가능할 수 있게 도와줌

# 클로저 사용 예제
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager # 함수 자체를 결과로 리턴
# 외부에서 호출된 함수의 호출이 끝나면 로컬 변수의 값은 저장되지 않지만 클로저 영역안의 자유변수는 값을 보존한다.

avg_closure1 = closure_ex1()
print(avg_closure1) # <function closure_ex1.<locals>.averager at 0x000002A92AC61440> 함수가 리턴
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))
print(avg_closure1(195))

print()

# 파이썬에서 자유변수를 어떻게 취급하고 있을까?
# function inspection
print(dir(avg_closure1)) # ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', ...]
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars) # ('series',)를 파이썬이 가지고 있다.
print()
print(avg_closure1.__closure__[0].cell_contents) # [10, 30, 50, 195] 저장되어있는 자유변수의 값을 출력
print()

# 잘못된 클로저 사용의 예
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager
avg_closure2 = closure_ex2()
# print(avg_closure2(10))
# UnboundLocalError: cannot access local variable 'cnt' where it is not associated with a value
# 할당되기 전에 사용했다는 에러가 발생한다. 위에 cnt 변수를 참조하지 못한다.

def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total # nonlocal로 선언해주면 자유변수가 된다. 누적 가능
        cnt += 1
        total += v
        return total / cnt
    return averager
avg_closure3 = closure_ex3()
print(avg_closure3(10))
print(avg_closure3(30))
print(avg_closure3(50))
print(avg_closure3(90))

