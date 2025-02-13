# 멀티 파일 읽기 : Read Multiple Files

'''
예제 1: /source/27-1/ 경로에 모든 텍스트 파일(txt)을 읽은 후 리스트로 출력
# 아래 조건 참조
파일명 & 경로 = "../source/27-1/*.txt"
출력 = ['Python', 'JavaScript', 'PHP', 'Rust', 'elite', 'Solidity', 'Assembly', 'hamster', 'india', 'january', 'kibana', 'lamada', 'monster', 'notion', 'orange', 'pokemon', 'query', 'range', 'sonic', 'telegram', 'urban', 'village', 'world', 'x-ray', 'yellow', 'zigzag']
'''

# 순서
# 1. 전체 리스트를 가져온다.
# 2. 리스트를 체크한다.
# 3. for 문을 통해 파일을 읽는다.

# 다양한 확장자 형식 파일 읽기는 중요하다.
# Python OS 패키지 사용은 능숙할 정도로 연습 필요
# 참조 : https://docs.python.org/3/library/os.html
# getcwd() : 현재 작업 경로를 반환
# listdir() : 지정한 경로의 파일 & 디렉토리 전부 반환

# 방법 1
import os

def read_text_file1(file_path):
    # 결과 리스트
    outputs = []

    # iterate through all file
    for file in os.listdir(file_path):
        # print(file)
        if file.endswith(".txt"): # 확장자 체크
            target_path = f"{file_path}/{file}" # 최종 경로 만들기
            # print(target_path) # 경로 확인
        with open(target_path, 'r') as f:
            # print(f.read()) # 내용 확인
            outputs.append(f.read().strip('\n'))
    return outputs

# 실행 1
print('ex1 결과 : ', read_text_file1("../source/27-1"))

# 방법 2 : glob 패키지도 사용 가능, 대부분 사용
# 참조 : https://docs.python.org/3/library/glob.html
import glob

def read_text_file2(file_path):
    # 결과 리스트
    outputs = []

    for file in glob.glob(file_path + '/*.txt'): # 위 방법보다 직관적이고 빠르다.
        with open(file, 'r') as f:
            # print(f.read()) 내용 확인
            outputs.append(f.read().strip('\n'))
    return outputs

# 실행 2
print('ex2 결과 : ', read_text_file2("../source/27-1"))