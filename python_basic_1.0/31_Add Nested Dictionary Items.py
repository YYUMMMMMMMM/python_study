# 중첩 Dict 추가 : Add Nested Dictionary Items

'''
예제 1: 아래 딕셔너리(Dict)에 두 개의 요소를 추가, 가능한 방법 모두 코딩
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

# 추가1
"group1" : {'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'}
    
# 추가2
"type" : {"f": "engineer"}

# 출력 결과
 {  "group1":[
                {'name': 'Park', 'age': '32', 'sex': 'Male'},
                {'name': 'Cho', 'age': '44', 'sex': 'Female'},
                {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'},
                {'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider", "f": "engineer"}
  }
'''

from pprint import pprint

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

# d.get('group1').append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'}) 
# d.get('type').update({"f": "engineer"})
# pprint(d)

# Dict update() 메소드
# List 추가에 append() 메소드
# 참고 : https://www.w3schools.com/python/python_dictionaries_add.asp

# 방법 1
# d['group1'].append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'})
# d['type'].update({"f": "engineer"})
# pprint(d)

# 방법 2
d.get('group1').append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'})
d.get('type')['f'] = "engineer"
pprint(d)