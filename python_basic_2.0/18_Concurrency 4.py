# Chapter06_04 병렬성(Parallelism) - Futures(동시성)
# Futures(동시성) : 파이썬 3.2부터
# 비동기 작업 처리
# 지연시간(Block), CPU 및 리소스 낭비 방지한다. 주로 (file)Network I/O 관련 작업 시 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능이 향상된다. (REST API)

# futures : 비동기 실행을 위한 API를 고수준으로 작성하고 사용하기 쉽도록 개선했다.
# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 API 통일하여 매우 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백함수 추가, 동기화 코드를 매우 쉽게 작성 > promise 개념

# 2가지 패턴 실습
# concurrent.futures 사용법 1
# concurrent.futures 사용법 2

# 파이썬 GIL : 두 개 이상의 스레드가 동시에 실행될 때 하나의 자원을 엑세스 하는 경우 문제점(이슈) 방지를 위해 GIL 실행
# 즉, 리소스 전체에 락이 걸린다. Context Switch(문맥 교환)
# 오히려 하나의 스레드를 사용할 때보다 느리게 실행수도 있다.
# 멀티프로세싱 사용, CPython 사용 시 GIL이 걸리지 않음

import os
import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # ProcessPoolExecutor
    # with futures.ThreadPoolExecutor() as executor:
    with futures.ProcessPoolExecutor() as executor:
        # concurrent.futures map
        # map -> 작업 순서 유지, 즉시 실행
        result = executor.map(sum_generator, WORK_LIST)

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\n Result -> {} Time : {:.2f}s'

    # 최종 결과 출력
    print(msg.format(list(result), end_tm))
    # Result -> [50005000, 5000050000, 500000500000, 50000005000000] Time : 0.77s
    # Result -> [5000050000, 500000500000, 50000005000000, 5000000050000000] Time : 8.61s -> ThreadPoolExecutor
    # Result -> [5000050000, 500000500000, 50000005000000, 5000000050000000] Time : 8.36s -> ProcessPoolExecutor

# 실행 시점
if __name__ == '__main__':
    main()

