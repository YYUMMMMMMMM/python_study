# 문자열 파싱 2 : String Split By Delimiter(Advanced)

'''
예제 1: /source 폴더의 22-2.txt 파일을 공백 구분 후 단어 개수를 출력하는 함수를 작성 후 실행, 콤마의 경우 두 단어로 취급
# Hi! Kim,Eun 의 경우 -> 3개
in_str = "../source/22-1.txt"
출력 결과 : 72
'''
in_str = 'The adjective "deep" in deep learning refers to the use of multiple layers in the network. Early work showed that a linear perceptron cannot be a universal classifier,but that a network with a nonpolynomial activation function with one hidden layer of unbounded width can. Deep learning is a modern variation which is concerned with an unbounded number of layers of bounded size,which permits practical application and optimized implementation,while retaining theoretical'

txt1 = in_str.replace(",", " ")
txt2 = txt1.split(" ")
# print(txt2)
print(f'출력 결과 : {len(txt2)}')

# string.split(separator, maxsplit) : 구분자, 분할 수
# string.replace(oldvalue, newvalue, count) : 타겟, 변환 값, 개수
# 콤마를 공백으로 치환 -> 문자열을 구분 후 리스트로 변환
# python re(Regular Expression) 사용가능(정규표현식)

# 방법 1
def cnt_word1(filepath):
    with open(filepath, 'r') as file:
        txt = file.read()
    txt = txt.replace(",", " ")
    
    # 쉼표 제거 확인
    # print(txt)

    # txt_list = txt.split()
    txt_list = txt.split(" ")

    # txt.split(" ")와 txt.split()의 동작에 미묘한 차이
    # txt.split()의 동작
    # 기본 구분자: split()은 모든 종류의 공백 문자(스페이스, 탭, 줄바꿈 등)를 구분자로 사용합니다.
    # 연속된 공백 처리: 연속된 공백은 무시됩니다.
    # 문자열 양끝의 공백 처리: 문자열의 양끝에 있는 공백도 제거됩니다.

    # txt.split(" ")의 동작
    # 구분자: " "(스페이스)만을 구분자로 사용합니다.
    # 연속된 공백 처리: 연속된 공백은 빈 문자열("")로 처리됩니다.
    # 문자열 양끝의 공백 처리: 문자열의 양끝 공백은 제거되지 않습니다.
    
    # 리스트 변환(공백)
    # print(txt_list)
    
    return len(txt_list)

print(f'ex1 결과 : {cnt_word1("../source/22-1.txt")}')

# 방법 2 : 정규표현식 사용
import re

def cnt_word2(filepath):
    with open(filepath, 'r') as file:
        txt = file.read()

    # 정규표현식 : 공백, 쉼표 제거 및 리스트 변환
    txt_list = re.split(" |,", txt) # 파이프라인 형태

    # 리스트 변환 (공백, 콤마) 확인
    # print(txt_list)

    return len(txt_list)

print(f'ex2 결과 : {cnt_word2("../source/22-1.txt")}')