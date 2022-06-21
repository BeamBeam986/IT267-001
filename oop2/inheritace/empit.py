from employee import Employyee

class EmpIT(Employyee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = ""
        self.departmeant = 'IT'

    def add_skill(self,skill:str):
        self.skill = skill


    def add_experience(self,experience:int):
        self.experience = experience


    def emp_detill(self):
        print('=== Employee IT Detail===')
        super().emp_detail() 
        print(f'skill:{self.skill}')
        print(f'experiene:{self.emp_detail}year(s)')
        #[รียกใช้ emp_detailของคลาส Employyee  แสดง id,name




    def it_salary(self):
        self._emp_salary()