# Chapter04_04 시퀀스
# 해쉬 테이블(Hashtable) > 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict > key 중복 허용 X, Set > 중복 허용 X
# Dict, Set 심화

# Immutable Dict 생성
from types import MappingProxyType

d = {'key1' : 'value1'} # 절대 수정되지 않아야 할 데이터라고 가정

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 가능
d['key2'] = 'value2'
print(d, id(d)) # {'key1': 'value1', 'key2': 'value2'} 1730388699456
print()
# 수정 불가
# d_frozen['key2'] = 'value2' # TypeError: 'mappingproxy' object does not support item assignment

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})
s3 = {3}
# s4 = {} # <class 'dict'>
s4 = set() # <class 'set'>
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')
print(s1) # {'Apple', 'Orange', 'Melon', 'Kiwi'}, 데이터 추가 가능

# 추가 불가
# s5.add('Melon')
# print(s5) # AttributeError: 'frozenset' object has no attribute 'add', frozenset()에는 add 메소드가 없다.

print(s1, type(s1)) # {'Kiwi', 'Apple', 'Melon', 'Orange'} <class 'set'>
print(s2, type(s2)) # {'Kiwi', 'Apple', 'Orange'} <class 'set'>
print(s3, type(s3)) # {3} <class 'set'>
print(s4, type(s4)) # set() <class 'set'>
print(s5, type(s5)) # frozenset({'Kiwi', 'Apple', 'Orange'}) <class 'frozenset'>

# Set 선언 최적화
# 바이트 코드 > 파이썬 인터프리터 실행
from dis import dis

print(dis('{10}'))
#   1           LOAD_CONST               0 (10)
#               BUILD_SET                1
#               RETURN_VALUE
# 3단계로 실행, 집합을 선언할 때 최적화하는 방법
print()
print(dis('set([10])'))
#   1           LOAD_NAME                0 (set)
#               PUSH_NULL
#               LOAD_CONST               0 (10)
#               BUILD_LIST               1
#               CALL                     1
#               RETURN_VALUE
# 6단계로 실행

# 지능형 Set(Comprehending Set)
print()
# print({chr(i) for i in range(0, 256)})
# {'Þ', '*', '\x03', 'I', 'Ù', '[', 'Q', '·', '£', 's', ...}
from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})
# {'', 'CIRCUMFLEX ACCENT', 'LATIN CAPITAL LETTER P', 'COMMA', 'YEN SIGN', 'DIGIT FOUR', ... }