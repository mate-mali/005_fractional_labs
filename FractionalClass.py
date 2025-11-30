class Fractional():
    
    x: int
    y: int

    def __init__(self, x:int, y:int):
        self.x = x
        if y == 0:
            raise ValueError("Y value of fractional cannoot be zero!")
        self.y = y

    
    def __str__(self):
        return f"{self.x}/{self.y}"
    
    def __repr__(self):
        return f"Fractional({self.x}, {self.y})"
    
    def __add__(self, fract):
        x_n = self.x * fract.y + self.y * fract.x
        y_n = self.y * fract.y
        return Fractional(x_n, y_n)
    
    def __mul__(self, fract):
        x_n = self.x * fract.x
        y_n = self.y * fract.y
        return Fractional(x_n, y_n)
    
    def __sub__(self, fract):
        x_n = self.x * fract.y - self.y * fract.x
        y_n = self.y * fract.y
        return Fractional(x_n, y_n)
    
    def __truediv__(self, fract):
        x_n = self.x * fract.y
        y_n = self.y * fract.x
        return Fractional(x_n, y_n)
    
    def to_decimal(self):
        return self.x / self.y


x1 = Fractional(1, 4)
x2 = Fractional(2, 3)

x3 = x1 + x2
print(x3)
print(x3.to_decimal())

x4 = x1 * x2
print(x4)
print(x4.to_decimal())

x5 = x1 - x2
print(x5)
print(x5.to_decimal())

x6 = x1 / x2
print(x6)
print(x6.to_decimal())

x7 = Fractional(20, 0)