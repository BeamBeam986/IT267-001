class Donkey:
    def __init__(self,age:int,weinght:float) -> None:
        self.age = 2
        self.weinght = 100

    def sound(self) -> None:
        return f'Donkey makes eeyore sound'

    def show_info(self):
        return f'{self.age} -year-old {self.weinght} kg'
        