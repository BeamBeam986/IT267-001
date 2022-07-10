class JuiceOrder:
    menu_type = "Juiceorder"
    total = 0
    def __init__(self,munu:str,size:str,price:int) -> None:
        self.munu = munu
        self.size = size
        self.price = 0

def check_menu(self):
        menu_dictionary= {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30,
        }
        
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

def compule_price(self):
        if self.size == 'R':
            self.price = 0
        elif self.size == 'L':
            self.price + 5
        else:
            self.price
        
        JuiceOrder.total = (self.price + self.size)


def display_order(self):
    self.check_munu()
    self.compute_price()
    return f' {self.menu} ,{self.size} +{self.price} => {JuiceOrder.total}'

def __del__(self):
        print("Object was destroyed")


if __name__ == "__main__":
    order1 ='WJ(L*35=> 35 baht'
    order2 ='OJ(L*25=> 25 baht'
    order3 ='PJ(L*35=> 35 baht'
    
    print(order1)
    print(order2)
    print(order3)