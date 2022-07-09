from geographic import Geographic
from temperature import Temperature
class Country(Geographic,Temperature):
    def __init__(self,name,area,population) -> None:
        super().__init__()
        self.name = name
        self.area = area
        self.population = population

    def getpopulationdensily(self):
        return self.population / self.area

    def showdetails(self):
        print (f'Conutry:{self.name}')
        print (f'locetion:{self.getcordinate()}')
        print (f'population:{self.population:,d}')
        print(f'area:{self.area:,.2f}')
        print (f'Density:{self.getpopulationdensily()}')
        print(f'timezone:{self.gettimezone()}')
        print(f'cliate:{self.getclimate()}')
        print(f'temperature:{self.getcelsius()}')
        print(f'temperature:{self.getfanrenheit()}')
        print(f'weather:{self.getweather()}')
        print('=============')
