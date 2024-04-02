# 랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0미만의 난수 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 난수 생성
print(int(random() * 10)) # 정수형으로 출력
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10) + 1)

print(randrange(1, 46)) # 1 ~ 46 미만의 임의값 생성
print(randint(1, 45)) # 1 ~ 45이하의 임의값 생성