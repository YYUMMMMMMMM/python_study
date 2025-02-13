# 시퀀스 타입 슬라이싱 : Sequence Type Slicing

'''
예제 1: 아래 리스트(List)에서 슬라이싱을 사용해서 [e,f,g] 값을 출력, 다양한 슬라이싱 방법으로 시도
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
출력 결과 : [e,f,g]
'''
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
print(f'출력 결과 : {x[4:7]}')
print(f'출력 결과 : {x[-9:-6]}')

# 시퀀스 자료형(데이터의 값이 연속적으로 이루어진 자료구조) : List, Tuple, Str, Range..
# List slicing : L[start:stop:step # step은 기본적으로 1이 생략되어있음
# 파이썬 언어 활용 극대화를 위해 리스트 자료구조는 매우 중요
# 기계 학습, 딥 러닝, 머신 머닝, 모델을 학습 시킬 때 중간에서 전처리를 할 때 리스트의 데이터를 꺼내거나 추가할 때 리스트 구조를 통해 이루어 짐 매우 중요
# 시간 복잡도 참고 : https://wayhome25.github.io/python/2017/06/14/time-complexity/

# 다양한 방법
print(f'출력 결과 : {x[4:-6]}')
print(f'출력 결과 : {x[-9:7]}')
print(f'출력 결과 : {x[-9:-6:1]}')
print(f'출력 결과 : {x[6:3:-1]}')
print(f'출력 결과 : {list(reversed(x[6:3:-1]))}')