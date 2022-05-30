
from re import T


class LingtSwitch():
    def __init__(self) -> None:
        self.switch_status= False

    def turnon(self):
        self.switch_status= True

    def turnon(self):
        self.switch_status= False

    def show(self):
        print (f'stutus = self.switch_status')

#สร้างวัตถุ object จากแม่พิมพ์ class
switch_obj = LightSwitch()
#เรียกใช้เมธอดฟังก์ชั้น
switch_obj.show() #F
switch_obj.turnon()
switch_obj.show() #T
switch_obj.turoff()
switch_obj.show() #f
switch_obj.turoff()
switch_obj.show()#f