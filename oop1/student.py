class Student:
    def __init__(self,id:str,name:str,majoy:str = "IT"):
        self.id = id
        self.name = name
        self.majoy = majoy

    def  display_detail(self):
        print(f'-----------------------------------')
        print(f'id:{self.id}')
        print(f'name:{self.name}')
        print(f'majoy:{self.majoy}')

    def __def__(self):
        print("obj Destroyed")

if __name__ == "__main__":
    jessica = Student('111','Jessica','IT')
    jessica.display_detail()

    John = Student('112','John','MKT')
    John.display_detail()

    amy = Student("113","Amy")
    amy.display_detail()