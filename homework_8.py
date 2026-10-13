from abc import ABC, abstractmethod
from os import name

'''
Абстрактный класс, чтобы не писать конструкцию if-else
Для защиты от создания экземпляра класса Flowers добавлен абстракный метод,
которого нет в требованиях
'''

class Flowers(ABC):
    def __init__(self, name, price, life_time):
        if price < 0:
            raise ValueError("Цена не может быть меньше нуля")
        if life_time <= 0:
            raise ValueError("Время жизни цветка должна быть положительным числом")
        self.__name = name
        self.__price = price
        self.__life_time = life_time

    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def life_time(self):
        return self.__life_time
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Цена не может быть меньше нуля")
        self.__price = new_price

    def __str__(self):
        return f'Название цветка: {self.name}\nСтоимость: {self.price}\nВремя жизни цветка: {self.life_time}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.life_time})"

    def __eq__(self, other):
        if not isinstance(other, Flowers):
            return False
        return self.name == other.name and self.price == other.price and self.life_time == other.life_time

    @abstractmethod
    def get_description(self):
        pass

'''
 Классы различных цветов
'''

class Rose(Flowers):
    def __init__(self, name, price, life_time):
        super().__init__(name, price, life_time)

    def get_description(self):
        return f'{self.name} - классический цветок с многослойными лепестками'

class Peony(Flowers):
    def __init__(self, name, price, life_time):
        super().__init__(name, price, life_time)

    def get_description(self):
        return f'{self.name} - пышный цветок с множеством мягких лепестков'

class Gerbera(Flowers):
    def __init__(self, name, price, life_time):
        super().__init__(name, price, life_time)

    def get_description(self):
        return f'{self.name} - яркий цветок, похожий на ромашку, с широкой палитрой оттенков'

class Chrysanthemum (Flowers):
    def __init__(self, name, price, life_time):
        super().__init__(name, price, life_time)
    def get_description(self):
        return f'{self.name} - пышный цветок с множеством тонких лепестков'


class Accessory:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Цена не может быть меньше нуля")
        self.__price = new_price

    def __str__(self):
        return (f'Название аксесуара: {self.name}\n'
                f'Стоимость: {self.price}')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price})"

class Bouquet:
    def __init__(self, name):
        self.__name = name
        self.__flowers = []
        self.__accessories = []
        self.__flowers_amount = 0


    @property
    def name(self):
        return self.__name

    @property
    def flowers(self):
        return self.__flowers

    @property
    def accessories(self):
        return self.__accessories

    def get_composition(self):
        return self.__flowers + self.__accessories

    def add_flowers(self, *args):
        self.__check_args(args, Flowers)
        for flower in args:
            if isinstance(flower, list):
                for element in flower:
                    self.__add_flower(element)
                    self.__flowers_amount += 1
            else:
                self.__add_flower(flower)
                self.__flowers_amount += 1

    def add_accessories(self, *args):
        self.__check_args(args, Accessory)
        for accessory in args:
            if isinstance(accessory, list):
                for element in accessory:
                    self.__add_accessory(element)
            else:
                self.__add_accessory(accessory)

    def get_flowers_cost(self):
        return round(sum(flower.price for flower in self.__flowers), 2)

    def get_accessories_cost(self):
        return round(sum(accessory.price for accessory in self.__accessories), 2)

    def get_total_cost(self):
        return self.get_flowers_cost() + self.get_accessories_cost()

    def get_life_time(self):
        return round(self.get_flowers_cost() / self.__flowers_amount, 2)

    def sort_by_price(self):
        return sorted(self.__flowers, key=lambda f: f.price)

    def is_consiste(self, name):
        for flower in self.__flowers:
            if flower.name == name:
                return True
        return False

    def __add_accessory(self, accessory):
        if not isinstance(accessory, Accessory):
            raise TypeError(f'Добавляемый элемент должен быть объектом {Accessory.__name__}')
        self.__accessories.append(accessory)

    def __add_flower(self, flower):
        if not isinstance(flower, Flowers):
            raise TypeError(f'Добавляемый элемент должен быть объектом {Flowers.__name__}')
        self.__flowers.append(flower)

    def __check_args(self, args, class_name):
        for element in args:
            if not isinstance(element, class_name):
                if not isinstance(element, list):
                    raise TypeError(f'Добавляемый элемент должен быть объектом {class_name.__name__}')



rose = Rose("Роза", 100.1, 3)
peony = Peony("Пион", 10.21, 3)
gerbera = Gerbera("Гербер", 102, 2)
chrysanthemum = Chrysanthemum("Хризантема", 103.4, 4)
lent = Accessory("Лента", 20)
otcritka = Accessory("Открытка", 15)
my_bouquet = Bouquet("Мой букет")
my_bouquet.add_flowers(peony, [gerbera, chrysanthemum], rose, [rose])
my_bouquet.add_accessories([lent])

print(my_bouquet.flowers)
print(my_bouquet.accessories)
print(my_bouquet.get_composition())
print(my_bouquet.sort_by_price())
print(my_bouquet.is_consiste("роза"))


