# minitask 6
class Point:
    def __init__(self, l=0, r=0):
        self.l = l
        self.r = r

    def __str__(self):
        return f"Point({self.l},{self.r})"

    def __sub__(self, other):
        return Point(self.l - other.l, self.r - other.r)


p0 = Point()
print(p0)  # should be: Point(0,0)
p1 = Point(3, 4)
result = p0 - p1
print(result)  # should be: Point(-3,-4)
