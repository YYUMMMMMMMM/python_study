# 알파벳 쓰기 : Alphabet in a File

'''
예제 1: source 폴더에 23-1.txt 파일 이름으로 대문자 알파벳(A-Z)을 공백으로 구분 후 파일로 작성

# 아래 조건 참조
파일명 & 경로 = "../source/23-1.txt"
파일 출력 결과 : "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
'''

# 파이썬 *유니코드*의 이해는 정말 중요
# 유니코드(Unicode) : 전세계에 존재하는 문자의 출력을 위한 인코딩 표준 -> 유니코드 코드값의 테이블 형태 
# ord(), chr() 함수 사용
# python string package : https://docs.python.org/3/library/string.html

# 방법 1 : 알파벳 리스트를 선언 후 파일로 쓰기
def write_alpabet1(filepath):
    with open(filepath, "w") as file:
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # Str은 시퀀스형이라 바로 써도 가능
            file.write(letter + " ")

print(f'ex1 결과 : {write_alpabet1("../source/23-1.txt")}')

# 방법 2 : string 패키지를 사용 후 쉽게 파일로 쓰기
import string # 원래 string은 내장함수이기 때문에 별도로 import 필요 없지만 이 경우에는 import를 해줘야 함

def write_alpabet2(filepath):
    # 예외 처리 생략
    with open(filepath, "w") as file:
        for letter in string.ascii_uppercase:
        # for letter in string.ascii_lowercase:
            file.write(letter + "\n")

print(f'ex2 결과 : {write_alpabet2("../source/23-2.txt")}')