
class UPIPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI")


class CreditCardPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "using Credit Card")


class WalletPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "using Wallet")


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


payment1 = Payment(UPIPayment())
payment1.make_payment(2000)

payment2 = Payment(CreditCardPayment())
payment2.make_payment(3000)

payment3 = Payment(WalletPayment())
payment3.make_payment(1000)
