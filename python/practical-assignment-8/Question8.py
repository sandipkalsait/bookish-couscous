class Quadrilateral:
    def __init__(self,l1,l2,l3,l4):
        self.l1=int(l1)
        self.l2=int(l2)
        self.l3=int(l3)
        self.l4=int(l4)
    
    def perimeter(self):
        return self.l1+self.l2+self.l3+self.l4

class Rectangle(Quadrilateral):
    def __init__(self, l1, l2, ):
        super().__init__(l1, l2, l1, l2)
    
    def calculate_area(self):
        return self.l1*self.l3


class Square(Quadrilateral):
    def __init__(self, l1):
        super().__init__(l1, l1, l1, l1)
    def calculate_area(self):
        return self.l1*self.l1*self.l1*self.l1
    
def driver1():
    lengthOfSquare=int(input("Enter the length any side of Square :\t"))
    square=Square(lengthOfSquare)
    print(f'the area of square is : {square.calculate_area()}')
    print(f'the perimeter of square is : {square.perimeter()}')
    # square.calculate_area()
    # square.perimeter()

def driver2():
    # pack and unpack concept in python
    # split runtime // not best  but fine for testing  
    length, width = map(int, input("Enter the length and width of rectangle (comma separated): ").split(","))
    rectangle = Rectangle(length, width)
    print(f'the area of rectangle is : {rectangle.calculate_area()}')
    print(f'the perimeter of rectangle is : {rectangle.perimeter()}')
    # square.calculate_area()
    # square.perimeter()

driver1()

driver2()




        