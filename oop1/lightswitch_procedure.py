#lightswitch_procedure
#สร้างฟังก์ชั่นเปิดไฟ
def turnon():
    global switch_status
    switch_status = True #เปิดไฟ

#สร้างฟังกืชั้นปิดไฟ

def turnon():
    global switch_status
    switch_status = False #ปิด

switch_status = False #ปิด


print(f'status = {switch_status}') #f
turnon()
print(f'status = {switch_status}') #t
turnon()
print(f'status = {switch_status}')#f
turnon()
print(f'status = {switch_status}')#f 