class Car:
    def ___init___(self,model,colour,year,price):
    self.model = model
    self.colour =colour 
    self.year =  year
    self.price = price

    def print_detail(self):
        print(f"Model:{model}")
        print(f"Colour:{colour}")
        print(f"year:{year}")
        print(f"price:{price}")


    @staticmethod
    def get_static_methot(text):
        print(f'String:{text}')

if __name__ == "__main__":
    my_car = Car("Cross","White",2022,1500000)
    #call instance method
    my_car.print_detail
    #call static method
    Car.get_static_methot("Hello Classs")
    my_car.get_static_methot("Hello Classs")




