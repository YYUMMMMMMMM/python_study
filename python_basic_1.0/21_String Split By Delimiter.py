# 문자열 파싱 1 : String Split By Delimiter
# 문자열 관련 함수는 실질적으로 굉장히 빈번하게 사용된다.
# 프로그램을 만들 때 파일을 읽어오거나 웹상의 정보를 크롤링해오거나, 자연어 처리나 감정분석을 사용해서 딥러닝에 활용하는데 기본이 되는 것이 텍스트이다.
# 텍스트를 내가 원하는 대로 전처리하는 능력이 필요하다.

'''
예제 1: 아래와 같은 문장을 공백으로 구분 후 단어 개수를 출력하는 함수를 작성 후 실행, input 함수 가능
in_str = "Suppose we have few words that are separated by spaces."
출력 결과 : 10
'''

in_str = "Suppose we have few words that are separated by spaces."
# print(in_str.split())
# print(len(in_str.split()))

def test(x):
    return len(in_str.split())
print(f'출력 결과 : {test(in_str)}')

# Python split() 함수는 자주 사용
# string.split(separator, maxsplit) : 구분자, 분할 수
# 기본 분리 지정자는 공백
# 문자열을 구분 후 리스트로 변환

# 방법 1
txt1 = "Suppose we have few words that are separated by spaces." # 시퀀스 형태
a = txt1.split()
print(a)
print(f'ex1 결과 : {len(a)}')

# 방법 2
txt2 = input()

b = txt2.split("&", 1)
print(b)
print(f'ex2 결과 : {len(b)}')