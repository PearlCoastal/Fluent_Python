from math import hypot
from typing import Any

class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(4, 5)
    
    print("加法运算，通过 __add__方法实现")
    v_add = v1 + v2
    print(v_add)
    
    print("乘法运算， 通过__mul__方法实现")
    v_mul = v1 * 3
    print(v_mul)
    