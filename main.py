from bank_account import BankAccount

accout1 = BankAccount('전은형', 150000)

accout1.money = -100000 # 누군가가 해킹했다

print('보유금액', accout1.money)