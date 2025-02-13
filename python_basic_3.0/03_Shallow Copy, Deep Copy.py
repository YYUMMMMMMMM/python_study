"""
Chapter 01
Python Advanced(1) - Shallow Copy, Deep Copy
Keyword - shallow copy, deep copy

"""
"""
객체 복사 종류 : Copy, Shallow Copy, Deep Copy
정확하게 이해 후 사용해야 프로그래밍 개발에 중요 (문제 발생 요소가 많다.)
가변(Mutable) : list, set, dict
불변(Immutable) : int, str, float, bool, unicode, ...

"""

# 예제 1 : Copy
# Call by Value, Call by Reffernce, Call By Share
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print('Ex1 > ', id(a_list)) # 3104343658432
print('Ex1 > ', id(b_list)) # 3104343658432
# 서로 같은 ID값

b_list[2] = 100
print('Ex1 > ', a_list) # [1, 2, 100, [4, 5, 6], [7, 8, 9]]
print('Ex1 > ', b_list) # [1, 2, 100, [4, 5, 6], [7, 8, 9]]

b_list[3][2] = 100
print('Ex1 > ', a_list) # [1, 2, 100, [4, 5, 100], [7, 8, 9]]
print('Ex1 > ', b_list) # [1, 2, 100, [4, 5, 100], [7, 8, 9]]

# 예제 2 : Shallow Copy
import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print('Ex2 > ', id(c_list)) # 2949662818112
print('Ex2 > ', id(d_list)) # 2949662719360
# 서로 다른 ID값

d_list[1] = 100
print('Ex2 > ', c_list) # [1, 2, 3, [4, 5, 6], [7, 8, 9]]
print('Ex2 > ', d_list) # [1, 100, 3, [4, 5, 6], [7, 8, 9]]

d_list[3].append(1000)
d_list[4][1] = 10000

print('Ex2 > ', c_list) # [1, 2, 3, [4, 5, 6, 1000], [7, 10000, 9]]
print('Ex2 > ', d_list) # [1, 100, 3, [4, 5, 6, 1000], [7, 10000, 9]]
# Shallow Copy : 중첩 리스트들은 같은 ID를 참조한다.

# 예제 3 : Deep Copy
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

print('Ex3 > ', id(e_list)) # 1463275603520
print('Ex3 > ', id(f_list)) # 1463275603584

f_list[1] = 100
print('Ex3 > ', e_list) # [1, 2, 3, [4, 5, 6], [7, 8, 9]]
print('Ex3 > ', f_list) # [1, 100, 3, [4, 5, 6], [7, 8, 9]]

f_list[3].append(1000)
f_list[4][1] = 10000

print('Ex3 > ', e_list) # [1, 2, 3, [4, 5, 6], [7, 8, 9]]
print('Ex3 > ', f_list) # [1, 100, 3, [4, 5, 6, 1000], [7, 10000, 9]]
# Deep Copy : 중첩 리스트들은 다른 ID를 참조한다.