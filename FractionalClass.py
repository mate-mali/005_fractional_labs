
class Fractional():
    
    x: int
    y: int

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x}/{self.y}"
    
    def __repr__(self):
        return f"Fractional({self.x}, {self.y})"
    
    def __add__(self, fract):
        x_n = self.x * fract.y + self.y * fract.x
        y_n = self.y * fract.y
    
        return Fractional(x_n, y_n)
    
    def to_decimal(self):
        return self.x / self.y


x1 = Fractional(1, 4)
x2 = Fractional(2, 3)
x3 = x1 + x2

print(x3)
print(x3.to_decimal())