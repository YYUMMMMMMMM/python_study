# Chapter06_05 병렬성(Parallelism) - Futures(동시성)
# Futures(동시성) : 파이썬 3.2부터
# 비동기 작업 처리
# 지연시간(Block), CPU 및 리소스 낭비 방지한다. 주로 (file)Network I/O 관련 작업 시 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능이 향상된다. (REST API)

# futures : 비동기 실행을 위한 API를 고수준으로 작성하고 사용하기 쉽도록 개선했다.
# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 API 통일하여 매우 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백함수 추가, 동기화 코드를 매우 쉽게 작성 > promise 개념

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# 파이썬 GIL : 두 개 이상의 스레드가 동시에 실행될 때 하나의 자원을 엑세스 하는 경우 문제점(이슈) 방지를 위해 GIL 실행
# 즉, 리소스 전체에 락이 걸린다. Context Switch(문맥 교환)
# 오히려 하나의 스레드를 사용할 때보다 느리게 실행수도 있다.
# 멀티프로세싱 사용, CPython 사용 시 GIL이 걸리지 않음

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [10000, 100000, 1000000, 10000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # futures
    futures_list = []

    # 결과 건수
    # ProcessPoolExecutor
    # with futures.ThreadPoolExecutor() as executor:
    with ProcessPoolExecutor() as executor:
        # concurrent.futures wait, as_completed
        for work in WORK_LIST:
            # future 반환
            future = executor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print('Sceduled for {} : {}'.format(work, future))

        # # wait 결과 출력
        # result = wait(futures_list, timeout=7)
        # # 성공
        # print('Completed Tasks : ', str(result.done))
        # # 실패
        # print('Pending ones after waiting for 7 seconds : ', str(result.not_done))
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\n Time : {:.2f}s'

    # 최종 결과 출력
    print(msg.format(end_tm))
    
# 실행 시점
if __name__ == '__main__':
    main()

# concurrent.futures wait : 여러 future 인스턴스들이 완료될 때까지 기다린다. timeout을 사용하여 반환하기 전에 대기할 최대 시간을 제어할 수 있다.
# concurrent.futures as_completed : 먼저 작업이 끝나는 future들이 반환된다. as_completed()가 호출되기 전에 완료한 모든 퓨처들이 먼저 yield 된다.