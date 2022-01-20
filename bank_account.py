class BankAccount:
    
    # 은행 계좌에는 예금주와 보유금액이 변수로 있음
    def __init__(self, user_name, money):
        self.user_name = user_name
        self.money = money