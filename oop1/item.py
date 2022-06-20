class Itim:
    def __init__(self,name:str,price:float,quantity:int) -> None:
        #รุุ้สินค้า ราคา จำนน
        assert price >= 1 , f"price should more than or equal to 1"
        assert quantity >= 1 , f"price should more than or equal to 1"
        self.name = name
        self.price = price
        self.quantity= quantity


    def calculate_total_price(self) -> None:
        #ราคาสิททธิ = ราคาสินค้า *จำนวนสินค้า
        return self.price * self.quantity



    def __del__(self) -> None:
       print("obj Destroyed")

if __name__ == "__main__":
    #create item
    item1 = Itim("cup",25,0)
    item2 = Itim("cone",10,3)
    print(f"****Total Price****")
    print(f"{item1.name}:{item1.calculate_total_price()}")
    print(f"{item2.name}:{item2.calculate_total_price()}")
