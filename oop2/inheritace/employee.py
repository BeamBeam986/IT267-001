class Employyee:
    def __init__(self,id,name,salary) -> None:
        self.id = id
        self.name = name
        self._salary = salary

    def emp_detail(self) -> None:
        print(f'id:{self.id}')
        print(f'name:{self.name}')

    def _emp_salary(self) -> None:
        print(f'salary: {self._salary}')



   