class Diagram:
    digram = "Student"
    def __inpuit___(self,id:str,name:str,majoy:str):
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
    #create jassica , john
    jessica = Student ("111","jesica","IT")
    jon = Student("112","Jon","MKT")
       
