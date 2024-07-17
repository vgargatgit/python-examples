from point import Point

p1 = Point(10, 20)

p4 = p1._replace(x=100)
print(p4)  # Output: Point(x=100, y=20)