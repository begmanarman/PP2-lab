import math

class Point:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
    
    def display(self):
       
        print(f"Point({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
       
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x1 = float(input("x1:"))
y1 =float(input("y1 :"))
p1 = Point(x1,y1)
p1.display()
x2 =float(input("x2:"))
y2 =float(input("y2:"))
p2=Point(x2,y2)
p2.display()
print( p1.dist(p2))


