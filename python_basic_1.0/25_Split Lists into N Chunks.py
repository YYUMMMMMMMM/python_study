# 리스트 스플릿 : Split Lists into N Chunks

'''
예제 1: 아래와 같이 주어진 리스트를 N개 단위로 출력 결과와 같이 리스트로 생성 & 출력, 함수 가능
# 기본 리스트
x = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# N -> 3
출력 결과 : [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R'],['S','T','U'],['V','W','X'],['Y','Z']]
    
# N -> 5
출력 결과 : [['A','B','C','D','E'],['F','G','H','I','J'],['K','L','M','N','O'],['P','Q','R','S','T'],['U','V','W','X','Y'],['Z']]
'''

# 기계 학습에서 np array 데이터 구조, 리스트 중첩이 깊은 뎁스로 되어있는 경우가 있다.
# 코딩 테스트에서도 많이 보임
# List slicing : https://www.geeksforgeeks.org/python-list-slicing/
# List Comprehension : https://www.w3schools.com/python/python_lists_comprehension.asp

# 기본 리스트
our_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 방법 1 : for loop
def split_n_list(split_size=3):
    split_list = list()

    for i in range(0, len(our_list), split_size):
        # 인덱스 확인
        # print(i, i + split_size)
        split_list.append(our_list[i:i+split_size])

    return split_list

print('ex1 결과 : ', split_n_list(3))

# 방법 2 : List Comprehension
split_size = 5

output = [our_list[i:i+split_size] for i in range(0, len(our_list), split_size)]
print('ex2 결과 : ', output)