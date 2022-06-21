from empit import EmpIT
from empmkt import EmpMKT

#create obj
mike = EmpIT("001","mike",60000)
mike.add_skill("Phython, JavaSrcipt")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()


#create 
anna = EmpMKT("002","Anna",35000)
anna.emp_detail()
anna.mkt_salary()

#พนังานการแผนตลาดชื่อ paul มีเงินเดือน 45000ได้รับคอมมิชชั่น 35%โดยทำงานอยู่จังหวัดเชียงใหม่
paul = EmpMKT("005","paul",45000)
paul.add_commission(35)
paul.add_location("chaigmai")
paul.emp_detail()
paul.mkt_salary()