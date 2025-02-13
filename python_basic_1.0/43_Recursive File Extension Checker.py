# 폴더 재귀 조회 : Recursive File Extension Checker

'''
예제 1: 폴더 43-1에 존재하는 파일 및 하위 폴더 전체에서 확장자가 *.txt 및 *.png 파일을 분류

# 폴더 경로
# ../source/43-1
# 조건1 : 텍스트 실행 형식(*.txt) 개수 및 파일명
# 조건2 : 이미지 파일 형식(*.png) 개수 및 파일명

# 출력 결과
TXT file info :  ['file1.txt', 'file14.txt', 'file15.txt', 'file2.txt', 'file20.txt', 'file5.txt', 'file7.txt', 'file9.txt', 'file1.txt', 'file6.txt', 'file7.txt', 'file8.txt']  Count :  12
PNG file info :  ['file10.png', 'file11.png', 'file19.png', 'file6.png', 'file3.png', 'file7.png', 'file3.png', 'file4.png']  Count :  8
'''

# os 패키지의 os.walk(), os.path.join(), listdir() 에서 필요한 함수를 사용.
# glob 패키지의 glob()함수를 사용.

# listdir() : os.listdir(path of the directory) 
# walk() : os.walk(top, topdown=True, onerror=None, followlinks=False)
# glob() : glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False)
    
# 참고1 : https://docs.python.org/3/library/os.html#os.listdir
# 참고2 : https://docs.python.org/3/library/os.html#os.walk
# 참고3 : https://docs.python.org/3/library/os.html#os.DirEntry.path
# 참고4 : https://docs.python.org/3/library/glob.html#glob.glob

# 방법 1
import os

txt_list1 = []
png_list1 = []

a = os.walk("../source/43-1")
# print(list(a)) # 리스트로 형변환 시 하위 폴더까지 순회하며 읽어 냄
for root, dirnames, filenames in os.walk("../source/43-1"):
    # print(root, ">>>", dirnames, ">>>", filenames)
    for f in filenames:
        ext = f.split(".")[-1]
        if ext == 'txt':
            txt_list1.append(f)
        if ext == 'png':
            png_list1.append(f)

print('TXT file info : ' , txt_list1, "Count : ", len(txt_list1))
print('PNG file info : ' , png_list1, "Count : ", len(png_list1))

# 방법 2
import glob

txt_list2 = glob.glob("../source/43-1/**/*.txt", recursive=True) # ** 하위 폴더까지 포함한다는 표현 recursive=True가 핵심이다.
png_list2 = glob.glob("../source/43-1/**/*.png", recursive=True)

print('TXT file info : ' , txt_list2, "Count : ", len(txt_list2))
print('PNG file info : ' , png_list2, "Count : ", len(png_list2))