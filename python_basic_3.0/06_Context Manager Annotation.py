"""
Chapter 02
Python Advanced(2) - Context Manager Annotation
Keyword - @contextlib.contextmanager, __enter__, __exit__

"""
"""
가장 대표적인 with 구문 이해
Contextlib 데코레이터 사용 : 코드가 직관적이고 예외 처리에 용이하다.

"""

# 예제 1 : File Writer, Use decorator

import contextlib
import time

@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f # __enter__
    f.close() # __exit__ : yield 바로 아래

with my_file_writer('testfile4.txt', 'w') as f:
    f.write('Context Manager Test4\nContextlib Test4')

# 예제 2 : Timer, Use decorator

@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try: # __enter__
        yield start
    except BaseException as e:
        print('Logging exception : {} : {}'.format(msg, e))
        raise
    else: # __exit__
        print('{} : {}s'.format(msg, time.monotonic() - start))

with ExcuteTimerDc('Start! job') as v:
    print('Received start monotonic 1 : {}'.format(v))
    # Excute job : 측정할 작업의 코드를 넣어주면 된다.
    for i in range(1000000):
        pass
    # raise ValueError('occurred.')
    # Logging exception : Start! job : occurred.