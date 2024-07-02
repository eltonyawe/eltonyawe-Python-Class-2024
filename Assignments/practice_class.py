class Shape:
    def __init__(self,color):
        self.color = color        

class Rectangle(Shape):
    def __init__(self, color,length,width):
        super().__init__(color)
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width

    def preimeter(self):
        return 2*(self.length+self.width)
    
    
color = input("Color : ")    
length =  int(input("length : "))    
width = int(input("Width : "))
    
rectangle = Rectangle(color,length,width)
print(f">>Color: {rectangle.color} >>Length : {rectangle.length}  >>Width : {rectangle.width}") 

   
print(f"Area : {rectangle.area()} \nPreimeter : {rectangle.preimeter()}")

        
            
        