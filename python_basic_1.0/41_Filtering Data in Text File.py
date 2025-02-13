# 텍스트 파일 필터링 : Filtering Data in Text File

'''
예제 1: 41-1.txt 텍스트 파일을 불러온 후 알파벳 C로 시작하는 나라의 지표의 합을 출력, 다양한 방법으로 해결
# 41-1.txt 파일을 열어보세요.

# C로 시작하는 나라 이름
# Canada, China, Chad ...

# 결과 값
1546447728
'''

# 다양한 포멧 형식(excel, txt, xml, html, json 등) 파일 데이터를 읽어오는 방법은 매우 중요.
# 사용자가 원하는 데이터의 합, 평균, 최대값, 최소값, 랭킹(정렬) 등 가공 능력
# 주로 pandas를 사용.
# 참고 : https://pandas.pydata.org/docs/reference/index.html

# 방법 1
def read_text_file1(file_path):
    # 결과 리스트
    value_list = []

    with open(file_path, 'r') as file:
        # print(file.read()) # 데이터를 그대로 가져옴
        # print(file.readline()) # 엔터를 기준으로 첫번째 데이터만 가져옴
        # print(file.readlines()) # 엔터를 기준으로 전체 데이터를 리스트로 가져옴
        lines = file.readlines()

        for line in lines:
            # country, value = line.split(",") # 줄바꿈이 있음
            country, value = line.rstrip().split(",") # rstrip(), 줄바꿈에 의한 공백 제거
            # print(country, value)
            if country.lower().startswith('c'): # if country.lower()[0] == 'c' 이렇게도 가능
                #print(country)
                value_list.append(int(value))

    return value_list
            
result = read_text_file1("../source/41-1.txt")
# print(result)
print(sum(result))

# 방법 2 : csv 패키지 활용
# 참고 : https://docs.python.org/3/library/csv.html
import csv

def read_text_file2(file_path):
    # 결과 리스트
    value_list = []

    with open(file_path, 'r') as file:
        
        # csv 형식 한 번에 읽기
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            # print(row)
            # print(row[0], row[1])
            # print(', '.join(row))
            
            if row[0].lower().startswith('c'):
                # 특정 문자열로 시작하는 국가 이름이 맞는지 확인
                # print(row[0])
                value_list.append(int(row[1]))
            
    return value_list

result = read_text_file2("../source/41-1.txt")

print(sum(result))
