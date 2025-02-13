# 실행 타임 딜레이 1 : Time Delays to Code
'''
예제 1: 1부터 10까지 1초 간격으로 숫자를 출력 후 종료, (while)문 사용 후 다양한 방법으로 시도
# 출력 결과
1
2
3
4
5
6
7
8
9
10
'''

import time

count = 1
while count < 11:
    print(count)
    count += 1
    time.sleep(1)

# for count in range(1, 11):
#     print(count)
#     count += 1
#     time.sleep(1)

# 일정 딜레이(시간) 간격 프로그램 실행 패턴 구현은 정말 중요
# 반복문 외 sleep 함수를 꼭 알아두어야 한다.
# time.sleep(secs)
# 참고 : https://docs.python.org/3/library/time.html#time.sleep

# 방법 1 # while문
# n = 0
# while n < 10: 
#     n += 1 
#     time.sleep(1)
#     print(n)

# 방법 2 # while True 특정 조건을 만족하면 종료되는 로직을 만들어 주어야한다. (break 사용)
# n = 0
# while True: 
#     n += 1 
#     time.sleep(1)
#     print(n)
#     if n == 10:
#         break

# 방법 3
# n = 1
# while True: 
#     time.sleep(1)
#     print(n)
#     n += 1 
#     if n > 10:
#         break


# 방법 4 : # break, continue문
# n = 1
# while True: 
#     time.sleep(1)
#     if n <= 10:
#         print(n)
#         n += 1 
#         continue
#     break