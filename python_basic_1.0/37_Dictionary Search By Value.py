# Dict 조회 : Dictionary Search By Value

'''
예제 1: 아래 Dict 데이터에서 사용자 입력으로 키(Key)로 검색 후 값을 반환

# Dict 선언
d = {'USA': 36, 'Germany': 17,'France':32, 'Australia': 77, 'South Africa': 99, 'India': 108, 'South Korea': 200}

# 사용자 입력1(정상 값)
France

# 출력1
'32'

# 사용자 입력2(잘못된 값)
Canada

# 출력2
'No results were found for your search.'
'''

# Dict 선언
d = {'USA': 36, 'Germany': 17,'France':32, 'Australia': 77, 'South Africa': 99, 'India': 108, 'South Korea': 200}

input_data = input("입력 :").lower()
# print(input_data)
def dict_search():
    for key, value in d.items():
        if input_data == key.lower():
            return value
            break
    else:
        return 'No results were found for your search.'
print(f'결과 : {dict_search()}')

# input 함수 사용
# 사용자 입력 기능을 구현 할 경우에는 다양한 입력 변수를 고려.(대소문자, 특수문자 등)
# 함수 형태로도 구현
# 예외 처리 기능을 사용하시면 기능적으로 견고하게 동작할 수 있다.
# 참고 : https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions

# 방법 1
# def search_dict(word):
#     try:
#         c = dict((new_k.lower(), new_val) for new_k, new_val in d.items()) # 키 값만 소문자로 변환하여 다시 딕셔너리를 만듬
#         # print(c)
#         return c[word]
#     except:
#         return '결과 : No results were found for your search.'
        
# txt = input("Enter key : ").lower()
# print(search_dict(txt))

# 방법 2
def search_dict(word):
    c = dict((new_k.lower(), new_val) for new_k, new_val in d.items())
    return c.get(word, "No results were found for your search.") # c.get()을 쓰면 자동으로 예외처리를 해줌
    
txt = input("Enter key : ").lower()
print(search_dict(txt))