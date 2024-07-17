from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])  # TypeName followed by list of field names in string

# Create an instance of Point
p = Point(10, 20)

print(p)         # Output: Point(x=10, y=20)
print(p.x, p.y)  # Output: 10 20