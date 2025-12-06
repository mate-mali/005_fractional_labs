class Fractional():
    
    x: int
    y: int

    def __init__(self, x:int, y:int = 1):
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
        return Fractional(x1.to_decimal()_n, y_n)
    
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
    
    def __lt__(self, fract):
        return self.to_decimal() < fract.to_decimal()
    
    def __gt__(self, fract):
        return self.to_decimal() > fract.to_decimal()
    
    def __le__(self, fract):
        return self.to_decimal() <= fract.to_decimal()
    
    def __ge__(self, fract):
        return self.to_decimal() >= fract.to_decimal()
    
    def __eq__(self, fract):
        return self.to_decimal() == fract.to_decimal()

x1 = Fractional(1, 4)
x1 = 1
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

x7 = Fractional(2,8)
print(f"{x1 = }")
print(f"{x1.to_decimal()}")

print(f"{x7 = }")
print(f"{x7.to_decimal()}")

print({x7.to_decimal()}, {x1.to_decimal()})

print(x1 == x7)
print(x1 > x2)
print(x1 < x2)
print(x1 >= x7)
print(x1 <= x7) 

#x7 = Fractional(20, 0)

#TODO: add handling whole numbers, addign with integers or other sht