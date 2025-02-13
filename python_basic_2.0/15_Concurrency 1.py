# Chapter06_01 병행성(Concurrency) - 기본
# 병행성, 흐름제어 설명

# 이터레이터(Iterator)와 제네레이터(Generator)
# 이터레이터(Iterator) : 반복 가능한 객체
# 제네레이터(Generator)는 이터레이터를 리턴한다.

# 파이썬 반복 가능한 타입
# collections, text, list, dict, set, tuple, unpacking, *args, ... : iterable 하다

# __iter__, __next__
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for c in t: 
    pass
    # print('for', c)
# t 내부적으로 iter() 함수를 호출하여 next()로 출력한 것
# 증명
# while
w = iter(t)
# print(dir(w)) # __iter__, __next__ 확인 가능
# print(next(w)) # A
# print(next(w)) # B
# print(next(w)) # C
# 출력된 데이터를 기억했다가 다음 데이터를 출력

while True:
    try:
        print('while', next(w))
    except StopIteration:
        break
print()
# 같은 결과를 출력한다.

# 반복형을 확인할 수 있는 방법
from collections import abc
print(dir(t))
print(hasattr(t, '__iter__')) # True
print(isinstance(t, abc.Iterable)) # True, Iterable을 상속받았는지 확인
print()

# 클래스 기반 제네레이터 구현 예제
# next 패턴
class Wordsplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
           raise StopIteration('Stopped Iteration')
        self._idx += 1
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = Wordsplitter('Do today what you could do tommorrow')
print(wi) # WordSplit(['Do', 'today', 'what', 'you', 'could', 'do', 'tommorrow'])
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi)) # StopIteration: Stopped Iteration
print()

# next 패턴은 불편 Generator 패턴을 사용해주자
# 1. 지능형 리스트, 딕셔너리, 집합을 만들 수 있다. 데이터 양이 증가 후 메모리 사용량이 증가하여 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터, 내부적으로 다음에 실행할 위치 정보를 기억하고 출력한다. 예외처리도 알아서 해줌
        return 'WordSplitGenerator(%s)' % (self._text)
    
wg = WordSplitGenerator('Do today what you could do tommorrow')
wt = iter(wg)
print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt)) # StopIteration: WordSplitGenerator(['Do', 'today', 'what', 'you', 'could', 'do', 'tommorrow'])
print()