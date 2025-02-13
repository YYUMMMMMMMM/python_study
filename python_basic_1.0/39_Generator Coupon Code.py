
# 쿠폰 코드 생성 : Generator Coupon Code
'''
예제 1: 주어진 문자열에서 6자리의 무작위의 코드를 중복없이 5개 생성 (리스트)
import random

# 문자열 선언
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
'''


# 랜덤으로 숫자 문자를 조합 후 중복없이 처리하는 방법도 중요.
# 실행 시 시간복잡도도 생각.

# UTC 기준 시간대 표현은 timezone 내장 모듈을 사용.
    
# random.choice : 1개 생성
# random.choices : 다수 생성(중복 없음) python 3.6+ 
# random.sample : 다수 생성(중복 있음)

# random.choice(seq)
# random.choices(population, weights=None, *, cum_weights=None, k=1)
# random.sample(population, k, *, counts=None)
    
# 참고 : https://docs.python.org/3/library/random.html
import random
from datetime import datetime

# 문자열 선언
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# 다양한 방식으로 프로그래밍 기능

# 난수 생성 : xorshit+, 선형합동법, CRC-32 encoding

# 중복 제거에 대한 고려가 필수
# 1. seed 사용
# 2. set() 사용
# 3. 반복문으로 중복 체크

# 방법 1 : seed 사용
def generate_coupon_code(n):
    code_list = []
    random.seed(None) # 과거에는 random.seed(datetime.now()) 이렇게 사용
    # random.seed(100) # seed 값이 고정인 경우 고정으로 나옴
    for i in range(0, n):
        chosen = random.sample(characters, 6)
        # print(chosen)
        code = "".join(chosen)
        code_list.append(code)
    return code_list
print(generate_coupon_code(5))