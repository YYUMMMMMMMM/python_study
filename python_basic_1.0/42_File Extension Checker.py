# 파일 확장자 체크 : File Extension Checker

'''
예제 1: 폴더 42-1에 존재하는 파일 중에서 확장자가 *.py 및 *.png 파일을 분류
# 폴더 경로
# ../source/42-1
# 조건1 : 파이썬 실행 형식(*.py) 개수 및 파일명
# 조건2 : 이미지 파일 형식(*.png) 개수 및 파일명

# 출력 결과
PNG file info :  ['file10.png', 'file11.png', 'file19.png', 'file6.png']  Count :  4
PY file info :  ['file12.py', 'file13.py', 'file17.py', 'file3.py', 'file4.py', 'file8.py']  Count :  6
'''


import os

png_files = []
py_files = []

def extension_check(file_path):
    for file in os.listdir(file_path):
        #print(file)
        if file.endswith('.png'):
            png_files.append(file)
            # print(png_file, len(png_file))
        if file.endswith('.py'):
            py_files.append(file)

    return png_files, py_files
extension_check("../source/42-1")
print(f'PNG file info : {png_files} Count : {len(png_files)}')
print(f'PY file info : {py_files} Count : {len(py_files)}')


# listdir() : os.listdir(path of the directory) 
# glob1() : glob.glob1(pathname)
# 참고1 : https://docs.python.org/3/library/os.html#os.listdir
# 참고2 : https://thomas-cokelaer.info/tutorials/python/module_glob.html

# 방법 1 : os 패키지의 listdir() 함수를 사용.

# files = os.listdir('../source/42-1')
# print(files)

png_list1 = []
py_list1 = []

for f in os.listdir('../source/42-1'):
    # print(f)
    # print(os.path.splitext(f)) # 파일명과 확장자를 스플릿하여 튜플 타입으로 반환
    # print(f.split('.')[-1]) # 확장자만 출력

    ext = f.split(".")[-1]

    if ext == 'png':
        png_list1.append(f)

    if ext == 'py':
        py_list1.append(f)

print('PNG file info : ' , png_list1, "Count : ", len(png_list1))
print('PY file info : ' , py_list1, "Count : ", len(py_list1))

print()

# 방법 2 : glob 패키지의 glob1()함수를 사용.
import glob

png_list2 = glob.glob1('../source/42-1', '*.png')
py_list2 = glob.glob1('../source/42-1', '*.py')

print('PNG file info : ' , png_list2, "Count : ", len(png_list2))
print('PY file info : ' , py_list2, "Count : ", len(py_list2))
