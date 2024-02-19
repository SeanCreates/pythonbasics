class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self,amount,recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES send to {recipient}")

        else:
            print("Insufficient amount send")


class personalmpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_no):
        super().__init__(account_balance, phone_number)
        self.id_no = id_no

    def buyairtime (self,amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought successfully")

class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_id):
        super().__init__(account_balance, phone_number)
        self.business_id = business_id

    def recieve_payment(self,amount):
            self.account_balance += amount
            print(f"{amount} KES received from a customer")

personal = personalmpesa(2000 , 797717013 , 240104  )
personal.send_money(3500, 724147892)
personal.buyairtime(2500)

business = BusinessMpesa(3000 , 705652520 , 543657)
business.send_money(2500 , 712345689)
business.recieve_payment (30000)
