# Chapter04_01 시퀀스
# 컨테이너(container : 서로 다른 자료형을 담을 수 있다. [list, tuple, collections.deque]) 컨테이너 자료형 예시 : a = [3, 3.0, 'a']
# 플랫(flat : 한개의 자료형만 담을 수 있다. [str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급 단계
# 지능형 리스트(Comprehending lists)
chars = '+_)(*&^%$#@!~)' # 플랫, 불변
# chars[2] = 'h' # TypeError: 'str' object does not support item assignment
code_list1 = []
for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# Comprehending lists : 속도 약간 우세
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending lists + Map, Filter
# 40 이상인 문자열만 가져옴
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성 (메모리 유지 X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))
print(type(tuple_g))
print(next(tuple_g)) # next()로 값을 한 개씩 반환할 수 있다.
print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))

print(array_g)
print(type(array_g))
print(array_g.tolist())
print()

# Generator 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
# 리스트 주의 (깊은 복사, 얕은 복사)
marks1 = [['~'] * 3 for n in range(4)] # 리스트 안의 리스트의 원소에 3를 곱하고 4번 반복
marks2 = [['~'] * 3] * 4
print(marks1) # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(marks2) # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1) # [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']], 각각의 리스트의 주소값이 다름
print(marks2) # [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']], 하나의 객체 주소값을 복사한 것, 동일한 주소값을 가져 모두 바뀜

# 증명
print([id(i) for i in marks1]) # [1809695979584, 1809695979776, 1809695979712, 1809695979968]
print([id(i) for i in marks2]) # [1809695979904, 1809695979904, 1809695979904, 1809695979904]



