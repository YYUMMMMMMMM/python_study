# Dict 반복문 활용 : Enumerate Dictionary

'''
예제 1: 아래 한 개의 리스트(List)를 딕셔너리(Dict) 형식으로 변환, 다양한 방법으로 시도
# 리스트
l = ["Red", "Green", "Black", "Blue", "Orange", "Purple"]

# 변환 결과1
{ 0: "Red", 1: "Green", 2: "Black", 3: "Blue", 4: "Orange", 5: "Purple" }

# 변환 결과2
{ 100: "Red", 101: "Green", 102: "Black", 103: "Blue", 104: "Orange", 105: "Purple" }
'''

# 파이썬 내장함수인 enumerate()는 열거형 객체를 반환 하고 카운터 변수도 추가
# 인덱스 생성 포함 출력 및 Dictionary 변환해도 자주 사용
# 반드시 알아두어야 하는 함수이다.
# enumerate(iterable, start=0)
# 참고 : https://docs.python.org/3/library/functions.html#enumerate

# 리스트
l = ["Red", "Green", "Black", "Blue", "Orange", "Purple"]

# 출력 1
d1 = dict(enumerate(l))
print(d1)

# 출력 2
d2 = dict(enumerate(l, start = 100))
print(d2)