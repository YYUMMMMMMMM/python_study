# Chapter07_02 : AsyncIO
# 비동기 I/O Coroutine 작업
# Generator > 반복적인 객체 Return 사용
# Non-blocking 비동기 처리

# Blocking I/O : 호출된 함수가 자신의 작업이 완료될 때까지 제어권을 가지고 있다. 다른 함수들은 대기해야 함
# NonBlocking I/O : 호출된 함수(서브 루틴)가 return 후 호출한 함수(메인 루틴)에 제어권을 전달한다. 다른 함수들은 작업을 지속

# 스레드 단점 : 디버깅, 자원 접근 시 레이스 컨디션(경쟁 상태), 데드락(Dead Lock)을 고려하여 코딩
# 코루틴 장점 : 하나의 루틴만 실행, 락 관리가 필요 없다. 제어권으로 실행
# 코루틴 단점 : 사용 함수가 비동기로 구현이 되어 있어야 하거나 직접 비동기로 구현해야 한다.

import asyncio
import timeit
from urllib.request import urlopen # urlopen : blocking
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import threading

# 실행 시작 시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장 (예 : 게시판성 커뮤니티)
urls = ['https://daum.net', 'https://naver.com', 'https://tistory.com']

async def fetch(url, executor):
    # 스레드명 출력
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url) # NonBlock으로 만들어 줌
    soup = BeautifulSoup(res.read(), 'html.parser')
    # 전체 페이지 소스 확인
    # print(soup.prettify())
    result_data = soup.title

    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)
    # 결과 반환
    return result_data

async def main():
    # 스레드풀 생성
    executor = ThreadPoolExecutor(max_workers=10)
    # future 객체를 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    # 결과 취합
    rst = await asyncio.gather(*futures) # list이기 때문에 unpacking

    print()
    print('Result : ', rst)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)