class BankAccount:
    
    # 은행 계좌에는 예금주와 보유금액이 변수로 있음
    def __init__(self, user_name, money):
        self.user_name = user_name
        self.money =money
        
        
    # money변수는 조회/변경 모두 추가적인 문장을 print해주자
    @property
    def money(self):   # money변수의 조회시에 대한 추가 기능 추가한것 (getter)
        print('누군가 금액을 조회합니다.')
        return self._money
    
    @money.setter
    def money(self, input_money):   # money변수에 값 대입시에 자동 실행될 코드를 추가(setter)
        print('누군가 금액을 변경합니다.')
        self._money = input_money