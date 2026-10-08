class ATM:
    def __init__(self, nom_20=0, nom_50=0, nom_100=0):
        self.nom_20 = nom_20
        self.nom_50 = nom_50
        self.nom_100 = nom_100

    def __is_int(self, *values):
        for i in values:
            if not isinstance(i, int) or isinstance(i, bool):
                return False
        return True

    def add_money(self, nom_20=0, nom_50=0, nom_100=0):
        if not self.__is_int(nom_20, nom_50, nom_100):
            raise ValueError("Количество купюр должно быть натуральным числом")
        self.nom_20 += nom_20
        self.nom_50 += nom_50
        self.nom_100 += nom_100

    def get_info(self):
        print(self.nom_20, self.nom_50, self.nom_100)

    def withdraw(self, amount):
        if not self.__is_int(amount) or amount <= 0:
            return False
        summ = self.nom_20*20 + self.nom_50*50 + self.nom_100*100
        if summ < amount or amount % 10 != 0:
            return False
        for i in range(min(amount // 100, self.nom_100), -1, -1):
            after_100 = amount - i*100
            for j in range(min(after_100 // 50, self.nom_50), -1, -1):
                after_50 = after_100 - j*50
                if after_50 % 20 == 0:
                    k = after_50 // 20
                    if k <= self.nom_20:
                        self.nom_100 -= i
                        self.nom_50 -= j
                        self.nom_20 -= k
                        print(f'Выдача:\nкупюры номиналом 100 - {i} шт.\n'
                              f'купюры номиналом 50 - {j} шт.\n'
                              f'купюры номиналом 20 - {k} шт.')
                        return True
        return False

bank = ATM(2)
bank.add_money(2,2, 1)
bank.get_info()
bank.withdraw(150)
bank.withdraw(40)
bank.get_info()