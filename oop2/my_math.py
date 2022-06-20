PI = 3.146

def square(number):
    #ruturn
    return (number ** 2)

def circle_area(radius):
    area = PI *radius*radius
    return area

if __name__ =='__mein__':
    print(square(5))
    print(circle_area(3))
    print(PI)