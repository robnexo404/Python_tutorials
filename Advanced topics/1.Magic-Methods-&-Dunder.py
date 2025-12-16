# Dunder means double underscore -> __
# Example __init__ in classes
class Vector:

    def __init__(self, x: int=1, y: int=1)-> None:
        self.x = x 
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self): # when the vector is being represented(printed for example), do this:
        return f"X: {self.x}, Y: {self.y}"
    
    def __len__(self):
        return 10 
    
    def __call__(self):
        print("hello, i was called")
    #these __ methods are magic methods
v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2

v3()

