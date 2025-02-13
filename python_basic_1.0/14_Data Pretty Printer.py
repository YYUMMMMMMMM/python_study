# 유용한 출력 함수 : Data Pretty Printer

from urllib import request
import json

response = request.urlopen("https://jsonplaceholder.typicode.com/users")

response_json = response.read()

d = json.loads(response_json)

# 출력 결과 비교(print)
# print(d)

# 출력 결과 비교(pprint)
# pprint : Python 데이터 구조를 예쁘게 인쇄할 때 사용하는 기능 제공
# 참고 : https://docs.python.org/3/library/pprint.html
from pprint import pprint

#pprint(d)

# depth(중첩 데이터), indent(들여쓰기), width(줄 길이 조정), sort_dicts(키 정렬), stream(파일에 출력) 옵션 제공
pprint(d, depth=3, indent=4, width=100)