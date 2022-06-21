from employee import Employyee

class EmpMKT(Employyee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'bangkok'
        self.commission = 30
        self.department = 'Marketing'

    def add_location(self,location):
        self.location = location

    def add_commission(self,commission):
        self.commission = commission

    def emp_detill(self):
        print('=== Employee Marketing Detail===')
        super().emp_detail() 
        print(f'location:{self.location}')
        print(f'commission:{self.commission}%')
        #[รียกใช้ emp_detailของคลาส Employyee  แสดง id,name

    def mkt_salary(self):
        self._emp_salary()

        