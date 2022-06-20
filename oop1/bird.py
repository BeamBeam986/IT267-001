#global
bird_type = 'perrot'

class Bird:
    #class var
    bird_name = 'Peter'
    def __init__(self,color) -> None:
        #instance
        self.color = color
        #local
        conutry = 'Thailand'
        print (conutry)

    def show(self):
        return f'{bird_type}{Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    print(f'****{bird_type}****')#เรียกใช้global
    my_bird = Bird('Red,yllow')
    print(my_bird.show())

    #เรียก class var
    #print(bird_name) Error

    #ชื่อclass
    print(Bird.bird_name)
    print(my_bird.bird_name)

