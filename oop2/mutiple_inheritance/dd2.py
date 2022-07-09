from dd import Person
class Sutdent(Person):
    def __init__(self, name,faculy,major,year:int) -> None:
        super().__init__(name)
        self.faculy = faculy
        self.major = major
        self.year = year
    
    def welcome(self) -> None:
        super().welcome()
        print(f'Welcome to {self.faculy} major {self.major}in {self.year}')
