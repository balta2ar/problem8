from math import sqrt
import matplotlib.pyplot as plt

class RightTriandle:
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("a and b must be positive")
        self.a = a
        self.b = b
        self.c = sqrt(a**2 + b**2)
    def plot_triangle(self):
        plt.figure(figsize=(8, 8))
        # plt.axis('equal')
        plt.plot([0, self.a, 0, 0], [0, 0, self.b, 0], 'k-')
        plt.show()

def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriandle(1, -1)
    except ValueError:
        success = True
    assert success

test_RightTriangle()
triangle1 = RightTriandle(1, 1)
triangle2 = RightTriandle(3, 4)
print(triangle1.c)
print(triangle2.c)
triangle2.plot_triangle()

