# Chapter06_03 병행성(Concurrency) - 코루틴, yield
# 코루틴(coroutine) : 단일(싱글)스레드에서 스택을 기반으로 동작하는 비동기 작업
# 스레드 : os에서 관리, CPU 코어에서 멀티스레드로 실시간, 시분할로 나눠 비동기 작업
# yield, send : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송
# 서브루틴 : 메인루틴 호출 후 서브루틴에서 수행(흐름 제어)
# 코루틴 : 루틴 실행 중에 중지, 중지 시점을 기억 후 재실행 -> 동시성 프로그래밍
# 코루틴 : 스레드에 비해 오버헤드가 감소한다.
# 스레드 : 싱글스레드, 멀티스레드 -> 코딩하기가 복잡하다 공유되는 자원이 교착 상태 발생 가능성이 있다. 컨텍스트 스위칭 비용이 발생하고 자원 소비 가능성이 증가한다.
# 비동기 처리 시 파이썬 3.5 이상에서 def -> async, yield -> await으로 사용 가능

# 코루틴 예제 1
def coroutine1(): # 코루틴은 제네레이터에서 파생됨, 단순히 함수라고 생각하지말고 함수 안의 코드를 확인하여 그 의도를 파악해야함
    print('>>> coroutine stared')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()
print(cr1, type(cr1)) # <generator object coroutine1 at 0x0000022ACB87B9F0> <class 'generator'>

# yield 지점까지 서브루틴 수행
# next(cr1) # 코루틴(서브루틴) 입장에서는 수동적임
# next(cr1) # >>> coroutine received : None 

# 기본 전달 값 None
# 값 전송
# cr1.send(100) # 메인루틴과 코루틴이 데이터를 교환할 수 있음 >>> coroutine received : 100

# 잘못된 사용
cr2 = coroutine1()
# cr2.send(100) # TypeError: can't send non-None value to a just-started generator, send() 명령어 바로 사용 불가
# next(cr1) 반드시 yield안에서 멈춘다음에 send()를 보내야 가능하다

# 코루틴 예제 2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태 (중요!, 이때 send() 값을 보내거나 받을 수 있다.)
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x # 데이터를 받음 = 데이터를 줌
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y # 데이터를 주고 받음
    print('>>> coroutine received : {}'.format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3)) # GEN_CREATED

print(next(cr3)) # >>> coroutine started : 10 , 10을 반환함

print(getgeneratorstate(cr3)) # GEN_SUSPENDED

cr3.send(100) # >>> coroutine received : 100, z를 받기위한 상태에 멈춰있음

print()
print()

# 코루틴 예제 3
# StopIteration 자동 처리(3.5 이상 -> await으로 자동 처리 됨)
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y
t1  = generator1()
print(next(t1)) # A
print(next(t1)) # B
print(next(t1)) # 1
print(next(t1)) # 2
print(next(t1)) # 3
# print(next(t1)) # StopIteration

t2 = generator1()
print(list(t2))

print()
print()

def generator2():
    yield from 'AB' # yield from : 제네레이터에서 이터레이블한 데이터를 순차적으로 끝날때까지 반환
    yield from range(1,4)

t3  = generator2()
print(next(t3)) # A
print(next(t3)) # B
print(next(t3)) # 1
print(next(t3)) # 2
print(next(t3)) # 3
# print(next(t3)) # StopIteration