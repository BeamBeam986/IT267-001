class Customer:
    def __init__(self) -> None:
        self.name = ''
        self.adddress = ''
        self.phone = ''
        

    def new_customer(self) -> None:
        self.name = input(('Enter customernamr name:'))
        self.adddress = input(('Enter customernamr address:'))
        self.phone= input(('Enter customernamr phoe:'))
    def cus_info(self) -> None:
        return f'{self.name}\nadddress:,{self.adddress}\nphone:,{self.phone}\nphone:'
