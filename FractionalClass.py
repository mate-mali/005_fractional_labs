
@dataclass(order=True)
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


x1 = Fractional(69, 420)
print(x1)
print(x1.__repr__())