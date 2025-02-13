# 날짜 및 시간 포맷팅 : Date Time Format By Strftime

'''
예제 1: datetime 패키지와 strftime 함수를 사용해서 하단 포맷 결과와 똑같이 출력
from datetime import datetime

t = datetime.now()

# 날짜 및 시간은 실행 시간에 따라 변경

# 출력 포맷1
# 2022-08-04 12:28:23

# 출력 포맷2
# 2022-08-04 12:28:23 PM Thursday August

# 출력 포맷3
# Thursday, August 04, 2022 12:28:57

# 출력 포맷4
# Thursday, Aug 08/04/22 12:28:57 PM
'''

# 다양한 형식의 시간 관련 출력 방법은 정말 중요
# 시, 분, 초, 일, 월, 년 간의 계산 방법도 꼭 알아두어야 한다.
# 날짜 계산, 수행시간 계산, 로그 출력 포멧 규정 등 프로그래밍에서 많이 활용. (특히 로그 출력 시 매우 중요)

# UTC 기준 시간대 표현은 timezone 내장 모듈을 사용.
    
# datetime.date.today() : 자주 사용
# datetime.now() : 자주 사용

# time.strptime(string[, format])
    
# 참고1
# https://docs.python.org/3/library/time.html#time.strptime
# https://strftime.org/
    
# 참고2
# https://docs.python.org/3/library/datetime.html

from datetime import datetime, timezone

# 타임존 출력
# print(datetime.now(timezone.utc))

t = datetime.now()
# print(t) # 2025-01-25 13:44:55.067482

# 출력 포맷 1
# 2025-01-25 13:52:19
print(t.strftime('%Y-%m-%d %H:%M:%S'))
# 01/25/25
print(t.strftime('%D'))
print(t.strftime('%x'))

# 출력 포맷 2
# 2025-01-25 13:53:30 PM Saturday January
print(t.strftime('%Y-%m-%d %H:%M:%S %p %A %B'))
# 2025-01-25 13:54:07 PM Sat Jan
print(t.strftime('%Y-%m-%d %H:%M:%S %p %a %b'))
# 02:00:17 PM
print(t.strftime('%r'))

# 출력 포맷 3
# Saturday, January 25, 2025 13:56:43
print(t.strftime('%A, %B %d, %Y %H:%M:%S'))
# 13:57:04
print(t.strftime('%T'))

# 출력 포맷 4
# Saturday, January 01/25/25 01:58:09 PM
print(t.strftime('%A, %B %x %r'))
# Saturday, January 01/25/25 13:58
print(t.strftime('%A, %B %x %R'))