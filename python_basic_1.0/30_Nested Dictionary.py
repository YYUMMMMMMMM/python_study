# 중첩 Dict : Nested Dictionary

'''
예제 1: 아래 딕셔너리(Dict)에서 출력결과와 같이 값을 추출, 가능한 방법 모두 코딩
# 중첩 Dict 선언
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

# 출력결과
Name : Kim, Age : 23, Type : officer
'''

# Dict 구조
# List는 Index를 사용해서 요소에 접근
# keys(), items(), get() 등 자주 사용하는 메소드는 꼭 기억
# 참고 : https://docs.python.org/3/tutorial/datastructures.html#dictionaries

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

# 방법 1
ex1 = 'Name : {0}, Age : {1}, Type : {2}'.format(d['group2'][0]['name'], d['group2'][0]['age'], d['type']['b'])
print(ex1)

# 방법 2 : get() 사용
ex2 = 'Name : {0}, Age : {1}, Type : {2}'.format(d.get('group2')[0].get('name'), d.get('group2')[0].get('age'), d.get('type').get('b'))
print(ex2)