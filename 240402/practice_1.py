# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(7*4)
print(3*3+2)

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
print('ㅋ'*8)

# boolean 자료형
print(5>10)
print(5<10)
print(True)
print(not True)
print(not False)
print(not(5>10))

# 변수
## 애완동물을 소개해주세요
animal = "강아지" #문자형이라서 큰 따옴표로 감싼다.
name = "배크진"
age = 4 #정수형은 따옴표나 큰 따옴표로 감싸지 않음.
hobby = "사진찍기"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "이예요")
##hobby = "공놀이"
print("" + name + "이는 " + str(age) + "살이며, " + hobby + "을(를) 아주 좋아해요") # +로 연결할 때는 정수형과 문자형 등을 선언해줘야 한다.
print("", name, "이는 어른일까요? ", is_adult, "") # ,로 연결할 때는 정수형이냐 문자형이냐에 상관없이 사용이 가능하다.

# 주석
'''여러문장을
주석처리 하는
방법은 이거!'''