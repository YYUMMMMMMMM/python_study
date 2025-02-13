# 파일 읽기 : Write Files Loops

'''
예제 1: /source/26-1/ 경로에서 아래 조건으로 name = 파일명, contents = 내용으로 파일로 작성
# 아래 조건 참조
파일명 & 경로 = "../source/26-1/파일명.txt"
파일명 리스트 = ["A", "B", "C", "D", "F", "G"]
컨텐츠 리스트 = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]
'''


# 다중 리스트 형태의 파일 쓰기 패턴은 정말 많이 사용한다.
# Python Open 함수의 쓰기 모드를 기억!
    
# 'w' : Open a text file for writing text (덮어쓰기)
# 'a' : Open a text file for appending text (추가) 
# f.write :  writes a string to a text file 
# f.writelines : write a list of strings to a file at once.

import os
# 운영체제(os) 위에서 파이썬, 자바 등 다양한 언어 사용, 결국 운영체제에 권한을 획득 받아야 사용 가능하다.
# 운영체제 기반에서 폴더를 만들거나 폴더가 있는 지 확인하거나 현재 작업 경로를 확인 등등 운영체제에 허락을 받아 가져와야한다.

filenames = ["A", "B", "C", "D", "F", "G"]
contents1 = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]
contents2 = [["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"],["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]]

# 방법 1
def write_contents1(filepath):
    if not os.path.exists(filepath): # 폴더 존재 여부 확인
        os.makedirs(filepath)
    # loop write
    for n, c in zip(filenames, contents1):
        with open(filepath + n + '.txt', 'w') as file:
            file.write(c)
# 실행 1
write_contents1("../source/26-1/")

# 방법 2
def write_contents2(filepath):
    if not os.path.exists(filepath): # 폴더 존재 여부 확인
        os.makedirs(filepath)
    # loop write
    for n, c in zip(filenames, contents2):
        with open(filepath + n + '.txt', 'w') as file:
            file.writelines(c + '\n' for c in c) # 리스트의 내용을 전부 다 순회하며 작성해준다.
# 실행 2
write_contents2("../source/26-2/")