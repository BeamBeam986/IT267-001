from donkey import *
from horse import Horse
class Mule(Donkey,Horse):
    def run(self):
        return f'Mule is running '
    def show_info(self):
        super().show_info()

if __name__=="__main__":
    mule1 =('*****Meme Info*****')
    mule1.name = 'MUMU'
    mule1.Color = 'Blue-eyed cream'
    mule1.Age = 3
    mule1.weight= 200


    mule2=('*****Meme Info*****')
    mule2.Name = 'Meme'
    mule2.Color = 'Palomino'
    mule2.MaxHeight = 200
    mule2.Age = 1
    mule2.weight= 120.7

print('=============')