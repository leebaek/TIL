# String Interpolation 문자열 보간법

# 1. 옛날 방식
# '%s %s' % ('one', 'two') #=> 'one two'

# 2. pyformat
# '{} {}'.format('one', 'two') #=> 'one two'

# name = '홍길동'
# eng_name = 'Hong'
# print('안녕하세요, {0}입니다. My name is {0}.'.format(name, eng_name))

# 3. f-string
# a, b = 'one', 'two'
# f'{a} {b}' #=> 'one two'

name = '홍길동'
print(f'안녕하세요, {name}입니다.')