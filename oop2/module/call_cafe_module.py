from cafe import Dessert,Drink
dessert_menu = Dessert()
print(dessert_menu.show_dessert())  

#แสดงรายการเครืื่องดื่ม
drink_munu = Drink()
print(drink_munu.show_drink())

#เพิ่มรายการเครื่องดื่ม
drink_munu.add_drink('juice')
drink_munu.add_drink('smoothy')
print(drink_munu.show_drink())