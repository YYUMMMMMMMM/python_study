# Dict 반복문 활용 : Iterate Dictionary

'''
예제 1: 아래와 같은 딕셔너리(Dict)를 출력 결과와 같이 완성 (반복문 사용)

Dict 선언
d = dict(one = list(range(1, 11)), two = list(range(11, 23)), three = list(range(23, 37)))

출력 결과 
key 'one' has values [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> total : 10
key 'two' has values [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] -> total : 12
key 'three' has values [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] -> total : 14
'''

# 애플리케이션을 만들 때 내가 원하는 형식으로 출력문을 만들어 낼 수 있어야 다양한 로그를 확인할 수 있다.

# Dict 선언
d = dict(one = list(range(1, 11)), two = list(range(11, 23)), three = list(range(23, 37)))

# 출력 결과
for k, v in d.items():
    print(f"key '{k}' has values {v} -> total : {len(v)}")

# Iterator : 순서대로 다음에 값을 반환(리턴)할 수 있는 객체 또는 상태(자체적으로 next 메소드 내장) 반복가능한 객체, 순회하면서 처리
# dict 구조의 items(), keys(), get() 함수를 기억
# https://www.w3schools.com/python/python_ref_dictionary.asp
