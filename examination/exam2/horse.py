class Horse:
    def __init__(self,max_height:float , name:str , color:str) -> None:
        self.max_height= 200
        self.name= 'khan khan'
        self.color= 'grey'
    
    def run(self) -> None:
        print(f'{self.name} is runing ')

    def show_name(self):
        print(f'{self.name}')
        
    def show_info(self) -> None:
        print(f'{self.name},{self.color},{self.max_height} cm')


    
