
'''
예제 1: 아래 문자열(JSON 구조)를 딕셔너리(Dict) 형식으로 변환
# Dict 선언
d = """
    {"group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }
    """


# 결과
{'group1': 
 [{'name': 'Park', 'age': '32', 'sex': 'Male'}, 
  {'name': 'Cho', 'age': '44', 'sex': 'Female'}, 
  {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
 ], 
 'group2': 
 [{'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'}, 
  {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
 ], 
 'type': {
     'a': 'employee', 'b': 'officer', 'c': 'director', 'd': 'manager', 'e': 'service provider'}
  }
'''

# JSON -> Dict 변환 : Convert JSON To Dictionary

# 문자열을(텍스트파일) Dictionary 구조로 변환하는 방법도 잘 알아두어야 한다.
# 데이터 송수신 부분에서 표준화된 데이터 포멧이기 때문이예요.(JavaScript Object Notation)

# json 내장 패키지를 통해 쉽게 변환 가능
# json.load() vs json.loads() 차이점을 꼭 이해

# json.loads()
# 목적: JSON 데이터를 문자열에서 읽어서 파이썬 객체로 변환
# 입력값: JSON 형식의 문자열
# 용도: 문자열 형태의 JSON 데이터를 파이썬 객체로 변환할 때 사용

# json.load()
# 목적: JSON 데이터를 파일 객체에서 읽어서 파이썬 객체로 변환
# 입력값: 파일 객체(예: open()으로 연 파일)
# 용도: JSON 형식으로 저장된 파일에서 데이터를 읽어올 때 사용

# json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
# json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    
# 참고
# https://docs.python.org/3/library/json.html#json.load

import json
from pprint import pprint
# """ """ 묶여있으면 JSON 형태로 가정할 수 있다.
d = """
    {"group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }
    """

result1 = json.loads(d.replace("'", "\"")) # JSONDecodeError: Expecting property name enclosed in double quotes : 바꾸어 주어야 함
pprint(result1)
print(type(result1))

# 방법 2
with open("../source/33-1.json", "r") as out:
    result2 = json.load(out)

    pprint(result2)
    print(type(result2))