# 폰북 프로젝트 : PhoneBook Project

'''
예제 1: 지금 까지 배운 내용을 기반으로 아래 조건과 같이 전화번호부를 while문을 사용 후 구현

# 구현내용
# 조건1 : 전화번호부 확인
# 조건2 : 전화번호부 멤버 추가
# 조건3 : 전화번호부 멤버 삭제
# 조건4 : 프로그램 종료
# 조건5 : 전화번호 전체 데이터는 아래와 같이 json 형식으로 가정
# 조건6 : (가능한경우) 파일 쓰기, 읽기 기능 추가

# 기본 제공 데이터
phonebook = {
                0: {'Name': 'Kim', 'Phone': '45648733'},
                1: {'Name': 'Lee', 'Phone': '89376333'},
                2: {'Name': 'Park', 'Phone': '36457818'},
                3: {'Name': 'Chung', 'Phone': '76891234'},
                4: {'Name': 'Choi', 'Phone': '67451237'}
            }
'''

import json
from pprint import pprint

# 기본 제공 데이터
phonebook = {
                0: {'Name': 'Kim', 'Phone': '45648733'},
                1: {'Name': 'Lee', 'Phone': '89376333'},
                2: {'Name': 'Park', 'Phone': '36457818'},
                3: {'Name': 'Chung', 'Phone': '76891234'},
                4: {'Name': 'Choi', 'Phone': '67451237'}
            }

filepath = '../source/45-1.json'

def phonebook_project(filepath):
    print('원하는 기능을 숫자로 입력하세요.\n1 : read | 2 : insert | 3 : delete | 4. exit')
    while True:
        user_input = input("기능 선택 : ")
        if user_input == '1':
            try:
                with open(filepath, 'r') as json_file:
                    data = json.load(json_file)
                    for key, value in data.items():
                        print(f'ID: {key}, Name: {value.get("Name")}, Phone: {value.get("Phone")}')
                    print("데이터를 불러왔습니다.")
            except (FileNotFoundError, json.JSONDecodeError):
                print("데이터가 없거나 파일을 찾을 수 없습니다.")
        elif user_input == '2':
            try:
                # 기존 데이터 읽기
                with open(filepath, 'r') as json_file:
                    data = json.load(json_file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}  # 파일이 없거나 JSON이 비어 있으면 빈 딕셔너리로 초기화

            num = input("id : ")
            name = input("name : ")
            phone = input("phone : ")

            if any(phone == value.get("Phone") for value in data.values()):
                print("해당 전화번호가 이미 존재합니다. 번호를 확인해주세요.")
                continue
            elif num in data:
                print("해당 ID가 존재하여 내용을 수정합니다.")
                
            data[num] = {'Name': name, 'Phone': phone}
            with open(filepath, 'w') as json_file:
                json.dump(data, json_file, indent=4)
                print(f"{name}의 데이터가 저장되었습니다.")
        elif user_input == '3':
            try:
                # 기존 데이터 읽기
                with open(filepath, 'r') as json_file:
                    data = json.load(json_file)
            except (FileNotFoundError, json.JSONDecodeError):
                print("삭제할 데이터가 없습니다.")
                continue

            num = input("삭제할 아이디를 입력하세요")

            if num in data:
                print("정말 삭제하시겠습니까?, 삭제 : 1, 취소 : 2")
                del_input = input("삭제 여부 : ")
                if del_input == '1':
                    del data[num]
                    with open(filepath, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                        print(f"ID {num}의 데이터가 삭제되었습니다.")
                elif del_input == '2':
                    print("삭제 취소")
                    continue
            else:
                print("해당 아이디가 없습니다.")
                continue
        elif user_input == '4':
            print('종료되었습니다.')
            break
        else:
            print('잘못 입력하셨습니다.')
            continue
phonebook_project(filepath)


# 기본 제공 데이터
# phonebook = {
#                 0: {'Name': 'Kim', 'Phone': '45648733'},
#                 1: {'Name': 'Lee', 'Phone': '89376333'},
#                 2: {'Name': 'Park', 'Phone': '36457818'},
#                 3: {'Name': 'Chung', 'Phone': '76891234'},
#                 4: {'Name': 'Choi', 'Phone': '67451237'}
#             }

# def list_phonebook(d):
#     """ List Member in phonebook. """
#     for pid in d:
#         print('\nPID', pid + 1)
#         for p_info in d[pid]:
#             print(p_info + ':', d[pid][p_info])

# def add_member(d):
#     """ Add a new member to the phone book."""
#     print("\nEnter the information of the member")
    
#     name = input('Name: ')
#     phone = input('Phone: ')
#     name_check = False
    
#     for pid in d:
#         if name == d[pid].get('Name'):
#             name_check = True
            
#     if name_check is True:
#         print('\n# The member is already in the phone book')
#     else:
#         d[len(d)] = {'Name': name, 'Phone': phone}
#         print('\n# The phone number has been added to the phone book')

#     return d
# def delete_member(d):
#     """ Delete a member from the phone book. """
#     print("\nEnter the name")
    
#     name = input('name: ')

#     for pid in d:
#         if name == d[pid].get('Name'):
#             del d[pid]
#             print('\n# The member has been deleted')
#             return d # 이 때는 리턴이 필수이다. 삭제완료 후 리턴문으로 프로그램을 종료하고 메인메뉴로 빠져나와야한다.
            
#     print('\n# The member is not in the phone book')
# def mainmenu():
#     while True:
#         menu = input("""
#         ----MAIN MENU----
#         1: List phonebook
#         2: Add a new member
#         3: Delete a member
#         4: Program exit 
#         Please enter your choice: """)

#         if menu == '1':
#             # print('1')
#             list_phonebook(phonebook)
#         elif menu == '2':
#             # print('2')
#             add_member(phonebook)
#         elif menu == '3':
#             # print('3')
#             delete_member(phonebook)
#         elif menu == '4':
#             # print('Exit')
#             break # return False
#         else:
#             print('\n Menu cannot be found')
# mainmenu()