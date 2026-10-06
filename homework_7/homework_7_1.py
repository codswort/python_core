class CreditCard:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть больше 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть больше 0")
        elif amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount

    def show_info(self):
        print(f'Номер вашего счета: {self.card_number}\nБаланс:{self.balance}')



try:
    card = CreditCard(2323, 100)
    card.show_info()
    card.deposit(10)
    card.show_info()
    card.withdraw(110)
    card.show_info()
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
