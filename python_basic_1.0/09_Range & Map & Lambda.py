# 자주 쓰이는 함수 3개 : Range & Map & Lambda

'''
예제 1: 아래와 같이 1부터 15까지 원소 * 10 결과는 문자열 리스트로 출력 (range, map, lambda 사용)
출력 결과 : ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140", "150"]
'''
result = list(map(lambda a: str(a * 10), filter(lambda a: a, range(1, 16))))
print(f'출력 결과 : {result}')

# 람다함수 : 인라인 작성으로 인해 가독성 증가(함수 표현식 내용이 적을 때 람다 사용 권장)
#            함수 객체 반환 -> 함수 객체 인수로 받는 map, filter 등과 연계 사용
# lambda : https://www.w3schools.com/python/python_lambda.asp
# map : https://www.geeksforgeeks.org/python-map-function/

# 방법 1
ex1 = []
for i in range(1, 16):
    ex1.append(str(i * 10))
print(f'ex1 결과 : {ex1}')

# 방법 2
ex2 = list(map(lambda x: str(x * 10), range(1, 16)))
print(f'ex2 결과 : {ex2}')

# 방법 3
ex3 = [str(x * 10) for x in range(1, 16)]
print(f'ex3 결과 : {ex3}')