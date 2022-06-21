from  cusorder.customer import Customer
from  cusorder.order import Order

#obj cus
cus1 = Customer("Jame","Bkk")
#order of cus
order1 = Order("15-06-2022","packed")
#display info
print(f'Order of {cus1.name} on {order1.date}is {order1.status}')