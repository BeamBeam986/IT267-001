#this file is intside bank 
#Call
from customer import Customer
from account import Account

cus1 = Customer()
cus1.new_customer()

cus1_acc = Account()
cus1_acc.open_account(cus1.name,"Saving",'10-123-456',500)
print("**** open Bank Account Detail****")
print(cus1.cus_info())
print(cus1_acc)