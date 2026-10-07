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
    card1 = CreditCard(2323, 100)
    card2 = CreditCard(2324, 200)
    card3 = CreditCard(2325, 300)

    card1.deposit(50)
    card2.deposit(50)
    card3.withdraw(70)

    card1.show_info()
    card2.show_info()
    card3.show_info()

except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
