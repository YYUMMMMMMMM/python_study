# 실행 타임 딜레이 2 : Progressive Time Delays to Code

'''
예제 1: 0.5부터 3까지 0.5초 간격으로 딜레이를 증가 하면서 아래와 같이 출력
# 출력 결과
Delayed for 0.5 seconds
Delayed for 1 seconds
Delayed for 1.5 seconds
Delayed for 2 seconds
Delayed for 2.5 seconds
Delayed for 3 seconds
'''

import time

delay = 0.5
for i in range(0, 6):
    time.sleep(delay)
    print(f'Delayed for {delay} seconds')
    delay += 0.5

while delay <= 3:
    time.sleep(delay)
    print(f'Delayed for {delay} seconds')
    delay += 0.5

# 일정 딜레이(시간) 간격 프로그램 실행 패턴 구현은 정말 중요
# 반복문 외 sleep 함수를 꼭 알아두어야 한다.
# sleep 구문이 포함된 1.함수 형태 또는 2.리스트 & 반복문을 사용해서 작성
# time.sleep(secs)
# 참고 : https://docs.python.org/3/library/time.html#time.sleep

# 방법 1
# for i in [.5, 1, 1.5, 2, 2.5, 3]:
#     time.sleep(i)
#     print(f'Delayed for {i} seconds')

# 방법 2
# n = .5
# while True:
#     time.sleep(n)
#     print(f'Delayed for {n} seconds')
#     n += 0.5
#     if n >= 3.5:
#         break

# 방법 3
# def sleep_out(n = 1):
#     print(f'Delayed for {n} seconds')
#     time.sleep(n)

# for n in [.5, 1, 1.5, 2, 2.5, 3, 3.5]:
#     sleep_out(n)

