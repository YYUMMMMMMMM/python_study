"""
Chapter 03
Python Advanced(3) - Descriptor 2
Keyword - descriptor vs property, low level(decriptor) vs high level(property)

"""
"""
디스크립터
1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. property와 달리 descriptor는 reuse(재사용) 가능
3. ORM Framework 사용

"""

# 예제 1 : descriptor 1
import os

# Descriptor 구현
class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        # print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))
    
class DirectoryPath:
    # Descriptor instance
    size = DirectoryFileCount()
    
    def __init__(self, dirname):
        self.dirname = dirname
        
# 현재 경로
s = DirectoryPath('./')
print(s.size) # 25

# 이전 경로
g = DirectoryPath('../')
print(g.size) # 24

# 헷갈릴 때 출력 용도
print('Ex1 > ', dir(DirectoryPath))
print('Ex1 > ', DirectoryPath.__dict__) # 'size': <__main__.DirectoryFileCount object at 0x000001A2E3E76900> DirectoryFileCount 객체의 주소값을 참조하고 있다.
print('Ex1 > ', dir(s))
print('Ex1 > ', s.__dict__)

# 예제 2 : descriptor 2 (로그 출력)
import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Descriptor 구현
class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value
    
    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value
    
    def __set__(self, obj, value):
        logging.info('Updating %r giving %r', 'score', self.value)
        self.value = value

class Student:
    # Descriptor instance
    score = LoggedScoreAccess()
    
    def __init__(self, name):
        # Regular instance attribute
        self.name = name
        
s1 = Student('yyummmmmmmm')
s2 = Student('LLeeeeeeeee')

# 점수 확인 (s1)
print('Ex2 > ', s1.score) # 2025-02-04 17:10:55 Accessing 'score' giving 50, 50
s1.score += 20
# 2025-02-04 17:11:18 Accessing 'score' giving 50
# 2025-02-04 17:11:18 Updating 'score' giving 50
print('Ex2 > ', s1.score) # 2025-02-04 17:10:55 Accessing 'score' giving 70, 70

print('Ex2 > ', s2.score)
s2.score += 30
print('Ex2 > ', s2.score)

# __dict__ 확인
print('Ex2 > ', vars(s1))
print('Ex2 > ', vars(s2))
print('Ex2 > ', s1.__dict__)
print('Ex2 > ', s2.__dict__)