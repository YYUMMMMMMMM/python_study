# Chapter04_02 시퀀스

# Tuple Advanced
# Unpacking
# b, a = a, b
print(divmod(100, 9)) # (11, 1)
# print(divmod((100, 9))) # TypeError: divmod expected 2 arguments, got 1
print(divmod(*(100, 9))) # (11, 1)
print(*(divmod(100, 9))) # 11 1
print()

# x, y, rest = range(10) # ValueError: too many values to unpack (expected 3)
x, y, *rest = range(10)
print(x, y, rest) # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(2)
print(x, y, rest) # 0 1 []
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest) # 1 2 [3, 4, 5]
print()

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l)) # (15, 20, 25) 2705600884352
print(m, id(m)) # [15, 20, 25] 1239942237888

l = l * 2
m = m * 2
print(l, id(l)) # (15, 20, 25, 15, 20, 25) 2705600506912
print(m, id(m)) # (15, 20, 25, 15, 20, 25) 2705600507104

l *= 2
m *= 2
print(l, id(l)) # (15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25) 2003850338960, ID값이 재할당
print(m, id(m)) # [15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25] 2003853040640, 가변형이기 때문에 원래 ID값에 할당됨, 변동이 심한 것들은 리스트에 담아두는 것이 좋음
print()

# sort vs sorted 경우에 맞게 잘 사용
# reverse, key=len, key=str.lower, key=func...
# sorted : 정렬 후 새로운 객체 반환 (원본을 수정하는 것이 아님)
f_list = ['ornage', 'apple', 'banana', 'mango', 'lime', 'melon']
print('sorted - ', f_list) # sorted -  ['ornage', 'apple', 'banana', 'mango', 'lime', 'melon']
print('sorted - ', sorted(f_list)) # sorted -  ['apple', 'banana', 'lime', 'mango', 'melon', 'ornage']
print('sorted - ', sorted(f_list, reverse=True)) # sorted -  ['ornage', 'melon', 'mango', 'lime', 'banana', 'apple']
print('sorted - ', sorted(f_list, key=len)) # sorted -  ['lime', 'apple', 'mango', 'melon', 'ornage', 'banana'] 
print('sorted - ', sorted(f_list, key=lambda x : x[-1])) # sorted -  ['banana', 'ornage', 'apple', 'lime', 'melon', 'mango']
print('sorted - ', sorted(f_list, key=lambda x : x[-1], reverse=True)) # sorted -  ['mango', 'melon', 'ornage', 'apple', 'lime', 'banana']

# sort : 정렬 후 객체를 직접 변경 (원본을 직접 수정)
# 반환 값 확인 (None)
print('sort - ', f_list.sort(), f_list) # sort -  None ['apple', 'banana', 'lime', 'mango', 'melon', 'ornage'], 원본이 수정되었음
print('sort - ', f_list.sort(reverse=True), f_list) # sort -  None ['ornage', 'melon', 'mango', 'lime', 'banana', 'apple']
print('sort - ', f_list.sort(key=len), f_list) # sort -  None ['lime', 'melon', 'mango', 'apple', 'ornage', 'banana']
print('sort - ', f_list.sort(key=lambda x : x[-1]), f_list) # sort -  None ['banana', 'lime', 'apple', 'ornage', 'melon', 'mango']
print('sort - ', f_list.sort(key=lambda x : x[-1], reverse=True), f_list) # sort -  None ['mango', 'melon', 'lime', 'apple', 'ornage', 'banana']

# list vs array 적합한 사용법 설명
# 리스트 기반 - list : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 - array : 배열(리스트와 거의 호환됨)

