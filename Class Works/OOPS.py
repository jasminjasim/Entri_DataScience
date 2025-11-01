class Department:
    def __init__(self, name,company, position):
        self.name=name
        self.company=company
        self.position=position

    def display(self):
        print(f"Department Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Position: {self.position}")
    
    # def getcompany(self):
    #     return self.__company

Analytics_department=Department("Analytics","Infosys","Data Scientist")
Analytics_department.display()



BackEnd=Department("Backend","TCS","Senior Developer")
BackEnd.display()




class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)
    
rect=Rectangle(10,5)
print("Area of Rectangle:",rect.area())
print("Perimeter of Rectangle:",rect.perimeter())

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)

    def area(self):
        return self.length*self.length
box=Square(5)
print("Area of Square:",box.area())
box.length=7
box.width=5

        



