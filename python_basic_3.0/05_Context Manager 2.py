"""
Chapter 01
Python Advanced(1) - Context Manager 2
Keyword - Contextlib, __enter__, __exit__

"""
"""
Contextlib = Measure execution(타이머) 제작

"""

# 예제 1 : Use Class

import time

class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg
    def __enter__(self):
        self._start = time.monotonic()
        return self._start
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print('Logging exception {}'.format((exc_type, exc_value, exc_traceback)))
        else:
            print('{} : {} s'.format(self._msg, time.monotonic() - self._start))
        return True # 명시적으로 작성
    
with ExcuteTimer('Start! job') as v:
    print('Received start monotonic 1 : {}'.format(v))
    # Excute job : 측정할 작업의 코드를 넣어주면 된다.
    for i in range(1000000):
        pass
    raise Exception('Raise! Exception') # 강제로 에러 발생
    # Logging exception (<class 'Exception'>, Exception('Raise! Exception'), <traceback object at 0x0000019E0FB32F40>)