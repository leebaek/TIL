# 1. dict 생성
lunch = {
    '중국집': '02-1108'
    '한식집': '02-4654'
}
lunch = dict(중국집='02') # 방법2

# 2. dict item 추가
lunch['분식집'] = '02-1748'

# 3. dict value 가져오기
lunch = {
    '한식집': {
        '고갯마루': '02-4981',
        '순남시래기': '02-9194'
    }
}
lunch['한식집'] # => {'고갯마루': '02-4981', '순남시래기': '02-9194'}
lunch['한식집']['고갯마루'] # => '02-4981'

# 추가. dict 내부 자료형
# key -> string, integer, float, boolean만 올 수 있음.
# value -> 모든 자료형이 올 수 있음.(list, dict..)

# 4. 딕셔너리 반복문 활용
lunch = {
    '한식집': '02-',
    '중식집': '031-',
    '일식집': '032-'
}
# 4-1. 기본
for key in lunch:
    print(key) # key
    print(lunch[key]) # value

# 4-2. key 반복
for key in lunch.keys(): # => ['한식집', ...]
    print(key)

# 4-3. value 반복
for value in lunch.values(): # => ['02-', '031-', ...]
    print(value)

# 4-4. key, value 반복
for key, value in lunch.items(): # => [('한식집', '02-'), ...]
    print(key)
    print(value)








