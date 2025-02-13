# Dict -> JSON 변환 : Convert Dictionary To JSON

'''
예제 1: 아래 딕셔너리(Dict)을 JSON 형식으로 변환
# Dict 선언
d = {"group1":[
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


# 결과
{
    "group1": [
        {
            "name": "Park",
            "age": "32",
            "sex": "Male"
        },
        {
            "name": "Cho",
            "age": "44",
            "sex": "Female"
        },
        {
            "name": "Kang",
            "age": "39",
            "sex": "Female",
            "married": "No"
        }
    ],
    "group2": [
        {
            "name": "Kim",
            "age": "23",
            "sex": "Male",
            "married": "Yes"
        },
        {
            "name": "Lee",
            "age": "37",
            "sex": "Male",
            "married": "No"
        }
    ],
    "type": {
        "a": "employee",
        "b": "officer",
        "c": "director",
        "d": "manager",
        "e": "service provider"
    }
}
'''

# Dict 선언
d = {"group1":[
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

import json
# print(f'{json.dumps(d, indent = 4)}')

# Dictionary 를 JSON으로 변환하는 기능은 정말 많이 사용
# 데이터 송수신 부분에서 표준화된 데이터 포멧이기 때문 (JavaScript Object Notation)

# json 내장 패키지를 통해 쉽게 변환 가능
# json.dumps() vs json.dump() 차이점을 꼭 이해 해야한다.

# json.dumps(dict, indent)
# 목적: 파이썬 객체를 JSON 형식의 문자열로 변환
# 반환값: JSON 형식의 문자열을 반환
# 용도: JSON 형식으로 변환된 데이터를 문자열로 다룰 때 사용

# json.dump(dict, file_pointer)
# 목적: 파이썬 객체를 JSON 형식으로 파일에 직접 쓰는 함수
# 반환값: 반환값은 없으며, 지정한 파일 객체에 JSON 데이터를 직접 기록
# 용도: JSON 데이터를 파일로 저장하고자 할 때 사용

# 참고
# https://docs.python.org/3/library/json.html

# 방법 1
# json_obj = json.dumps(d, indent = 4)
# print(json_obj)

# 방법 2
with open("../source/32-2.json","w") as out:
    json.dump(d, out)
    