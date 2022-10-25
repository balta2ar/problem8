from math import cos, sin, pi
import matplotlib.pyplot as plt

class F:
    def __init__(self, n, m):
        self.n = n
        self.m = m
    def __call__(self, x):
        return cos(self.n * x) + sin(self.m * x)

u = F(5, 2)
v = F(2, 3)
plt.figure(figsize=(8, 8))
xs = [x*pi/180.0 for x in range(100)]
apply = lambda f: [f(x) for x in xs]
plt.plot(apply(u), apply(v), 'k-')
plt.show()
