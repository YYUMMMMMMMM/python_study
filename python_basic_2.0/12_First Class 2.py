# Chapter05_02 일급함수(First-Class) - 클로저(Closure) 기초

# 파이썬 변수 범위(Scope)
# 예제 1
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) # NameError: name 'b' is not defined

# 예제 2
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)

# 예제 3 Global 선언
c = 30

def func_v3(a):
    global c # 함수 내에서 global로 값을 변경하는 것은 좋은 방법이 아니다.
    #c = 40
    print(a)
    print(c)
    c = 40

# func_v3(10)
# UnboundLocalError: cannot access local variable 'c' where it is not associated with a value c 할당 전에 참조하기 때문에 에러 발생
# Local 변수로 인식한다.

print('>>', c)
func_v3(10)
print('>>>', c) # 위 함수에서 c값이 글로벌 키워드로 40으로 재할당 되었음

# 클로저(Closure) 사용 이유
# 상태(불변상태)를 기억한다!
# 서버 프로그래밍에서 중요한 부분이 동시성(Concurrency) 제어이다. 한정된, 같은 메모리 공간에 여러 자원이 접근하면 교착상태(Dead Lock)가 됨
# 파이썬에서는 이런 문제를 회피하기 위해서 메모리를 공유하지 않고 메시지 전달로 처리
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 구조를 적극적으로 사용 -> 함수형 프로그래밍과 연결됨
# 클로저는 불변자료구조 및 atom, STM을 통해 멀티스레드(Coroutine) 프로그래밍에 강점

# 예제 1
a = 100
print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v): # 클래스를 함수처럼 호출할 수 있다.
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)
    
# 인스턴스 생성
averager_cls = Averager()

# 누적
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(195))
# 함수 호출 후 끝이나도 기억하고 계속해서 누적되고 있다.