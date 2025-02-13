"""
Chapter 01
Python Advanced(1) - Context Manager 1
Keyword - Contextlib, __enter__, __exit__, exception

"""
"""
운영체제의 자원은 한정 되어있다. 그래서 open했으면 close해줘야 자원의 낭비를 막을 수 있다.
Context Manager : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할을 한다.
Context Manager의 가장 대표적인 예 with 구문을 이해해한다.
문제 발생 요소를 감소시키기 위해 정확한 이해 후 프로그래밍에 사용해야한다.

"""
# 예제 1

file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1\nContextlib Test1.')
finally:
    file.close()

# 예제 2 : with
with open('./testfile2.txt', 'w') as f:
    f.write('Context Manager Test2\nContextlib Test2.') # 굳이 close 해주지 않아도 with문 사용 시 내부적으로 자동으로 close 해준다.

# 예제 3 : 클래스로 with 직접 구현
# Use Class -> Context Manager with exception handling.
# 클래스로 구현 시 예외 처리가 쉽다.

class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)
    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj
    def __exit__(self, exc_type, value, trace_back):
        print('MyFileWriter started : __exit__')
        if exc_type:
            print('Logging exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()

with MyFileWriter('./testfile3.txt', 'w') as f:
    f.write('Context Manager Test3\nContextlib Test3.')
