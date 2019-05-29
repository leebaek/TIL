def hello(func):
    print('hihi')
    func() # => bye()
    print('hihi')


@hello # 데코레이터 : 함수를 parameter로 받는 것
def bye():
    print('bye bye')

bye()
