# Chapter04_03 시퀀스

# 해쉬 테이블(Hashtable)
# 해시값이 중복되었을 때 처리 방법 이런 질문들을 많이 함
# 해쉬 구조 : key에 value를 저장하는 구조
# 파이썬 dict 해쉬 테이블의 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조!
# key 값을 해싱 함수를 통해 해쉬 주소값을 반환하고 이를 기반으로 key에 대한 value를 참조할 수 있다.

# Dict 구조
# print(__builtins__.__dict__) # key:value 구조를 가지고 있다.

# Hash값 확인, 해쉬값을 확인할 수 있다는 것은 고유하다는 뜻
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
print(hash(t1)) # 465510690262297113, 불변한 tuple이기 때문에 고유한 해쉬값을 추출할 수 있다.
# print(hash(t2)) # TypeError: unhashable type: 'list' list는 해쉬값을 추출할 수 없다. list는 가변하기 때문에 고유하지 않음

# Dict 생성 고급 예제

# Setdefault 사용법
# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1) # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2) # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

# 주의사항
new_dict3 = {k : v for k, v in source}
print(new_dict3) # {'k1': 'val2', 'k2': 'val5'} 키가 중복될 경우 마지막 값으로 덮어써버림