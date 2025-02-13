# Chapter06_02 병행성(Concurrency) - 제네레이터
# 병행성(Concurrency) : 한 컴퓨터(하나의 CPU, 하나의 스레드)가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 파이썬의 장점, 코루틴이 병행성을 구현해 줌
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# 제네레이터 예제 1 : yield 실습
def generator_ex1():
    print('Start')
    yield 'A Point' # 다음에서 크롤링
    print('Continue')
    yield 'B Point' # 네이버에서 크롤링
    print('End')

temp = iter(generator_ex1())
# print(temp)
# print(next(temp))
# 다른 일을 처리하다가 밑에서 다시 호출해주면 이어서 작업이 가능
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass
    # print(v)

# 제네레이터 예제 2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1()) # 따로 반복을 돌려줘야 됨

# print(temp2) # ['A PointA PointA Point', 'B PointB PointB Point']
# print(temp3)

for i in temp2:
    print(i)

for i in temp3:
    print(i)

print()
print()

# 제네레이터 예제 3 : itertools 중요 함수
# count, takewhile, filterfalse, accumulate, chain, product, groupby, ...

import itertools

# count, takewhile
gen1 = itertools.count(1, 2.5) 
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# itertools.count() : 무한대로 출력, while문 True에 놓고 사용하면 무한 루프

gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))
for v in gen2:
    pass
    # print(v)

# filterfalse : 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    pass
    # print(v) # 3미만의 반대값 출력

# accumulate : 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 1001)])
for v in gen4:
    pass
    # print(v)

# chain : 연결 1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
# print(list(gen5))

# chain : 연결 2
gen6 = itertools.chain(enumerate('ABCDE'))
# print(list(gen6)) # 튜플형 리스트로 출력

# product : 개별 
gen7 = itertools.product('ABCDE')
# print(list(gen7))

# product repeat : 연산(경우의 수), 모든 경우의 수를 출력
gen8 = itertools.product('ABCDE', repeat=2)
# print(list(gen8))

# groupby : 그룹화
gen9 = itertools.groupby('AAAAAABBBBBCCCCDDDEEEE')
# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))