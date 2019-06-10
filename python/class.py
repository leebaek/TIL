class Person:
    name = '사람의 고유한 속성'
    age = '출생 이후부터 삶을 마감할 때 까지의 기간'

    def greeting(self): # method를 정의하면 self인자가 자동으로 들어간다.
        print(f'{self.name}이 인사합니다. 안녕하세요.')

    def eating(self):
        print(f'{self.name}은 밥을 먹고 있습니다.')

    def aging(self):
        print(f'{self.name}은 현재 {self.age}살이고, 현재 나이를 먹어가는 중입니다.')

peter.name == self.name

peter = Person() # Person이라는 클래스로부터 peter라는 인스턴스를 생성한 것!
print(peter.name)
print(peter.age)
peter.name = 'peter'
peter.age = '19'
print(peter.name)
print(peter.age)
peter.greeting()
peter.eating()
peter.aging()