from vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__year = 0
        self.__maintanance = 0

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        self.__year = value

    @property
    def maintanance(self):
        return self.__maintanance
    @maintanance.setter
    def maintanance(self,value):
        self.__maintanance = value

    def show_detail(self):
         super().show_detail()
         print ('====Car Detail====')
         print(f'{self.brand} witn speed {self.speed}')
         print(f'manufactered in {self.year} has {self.gear} gear and {self.seat} seats.')

    def show_maintanance(self):
        print('====Car Maintanance====')
        print(f'the lastest {self.brand}--{self.year} maintanace in {self.maintanance}')
        
class Truck(Vehicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__capacity = 1000
        self.__wheel = 4

    @property
    def capacity(self):
         return self.__capacity
    @capacity.setter
    def capacity(self,value):
        self.__capacity = value

    @property
    def wheel(self):
        return self.__wheel
    @wheel.setter
    def wheel(self,value):
        self.__wheel = value

    def show_detail(self):
         super().show_detail()
         print ('++++ Truck+++')
         print (f'{self.brand} with speed {self.speed} km/hr and {self.wheel} can carry {self.capacity}tons.')
    
    def show_price(self):
        if self.wheel == 4:
            price = 1000
        elif self.wheel == 6:
            price = 2000
        else :
            price =3000
        
        print(f'{self.wheel} truck is {price} baht/day')
