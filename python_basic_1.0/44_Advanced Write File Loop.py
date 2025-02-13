# 파일 읽기 & 쓰기 고급 : Advanced Write File Loop

'''
예제 1: 아래 조건과 같이 ../source/44-1.txt에 파일 읽기 및 쓰기 기능을 while문을 사용 후 구현

# 구현내용
# 조건1 : 파일명 및 위치 ../source/44-1.txt
# 조건2 : 사용자 입력 (쓰기, 읽기, 종료)
# 조건3 : 기존 내용에 추가해서 쓰기 수행
# 조건4 : "종료" 명령어 입력 전까지는 프로그램이 종료 불가
# 조건5 : 파일 내용은 \n(줄바꿈) 해서 출력 수행
'''

import os

def file(filepath):
    print('원하는 기능을 숫자로 입력하세요.\n1 : read | 2 : write | 3 : exit')
    while True:
        user_input = input("기능 선택 : ")
        if user_input == '1':
            with open('../source/44-1.txt', 'r') as file:
                print(file.read())
        elif user_input == '2':
            with open('../source/44-1.txt', 'a') as file:
                write_input = input("작성 내용 : ")
                file.write(write_input + '\n')
        elif user_input == '3':
            print('종료되었습니다.')
            break
        else:
            print('잘못 입력하셨습니다.')
            continue
file('../source/44-1.txt')

# Python File I/O Mode 이해
# open("source", a+) : write in text mode(appending, reading and writing)
# open("source", w+) : write in text mode(reading and writing)
# open("source", r+b) : read and write in binary mode
# 참고 : https://docs.python.org/3/library/functions.html#open

# 방법 1
# file mode에 주의

# filepath = '../source/44-1.txt'
# intro = "Select a menu number : "
# file = open(filepath, "a+") # 읽기, 쓰기 가능

# while True:
#     print("---------------")
#     print("1. read")
#     print("2. write")
#     print("3. exit")
#     print("---------------")
#     menu = int(input(intro))
    
#     if menu == 1:
#         file = open(filepath, 'r') # 정확하게 명시해줌 안해도 괜찮다.
#         print(file.read())
#         file = open(filepath, 'a+') # 모드 변경
#         print()
#         print("---------------")
#         print("읽기 완료")
#         print("---------------")
#     elif menu == 2:
#         text = input("작성 : ")
#         file.write(text + '\n')
#         print()
#         print("---------------")
#         print("쓰기 완료")
#         print("---------------")
#     elif menu == 3:
#         file.close() # close() 해줘야 함, with문을 사용한다면 안해줘도 괜찮음 with문을 빠져나갈 때 자동으로 close해줌
#         print()
#         print("---------------")
#         print("종료")
#         print("---------------")
#         break