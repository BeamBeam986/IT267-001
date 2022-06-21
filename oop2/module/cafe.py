class Dessert:
    def __init__(self) -> None:
        self.dessert = ['ice cream','sticky rice mango']

    def show_dessert(self) -> None:
        return f'Dessert:{self.dessert}'

class Drink :
    def __init__(self) -> None:
        self.drink = ['coffe','tea','wine','soda']

    def add_drink(self,new_drink:str) -> None:
        self.drink.append(new_drink)

    def show_drink(self) -> None:
        return f'Drink:{self.drink}'