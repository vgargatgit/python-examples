from point import Point

class PointWithDefaults(Point):
    __slots__ = ()  # This ensures no per-instance dict is created
    def __new__(cls, x=0, y=0):  # x and y default to 0 
        return super(PointWithDefaults, cls).__new__(cls, x, y)

# Create points with default values
p1 = PointWithDefaults()
p2 = PointWithDefaults(5)
p3 = PointWithDefaults(5, 10)

print(p1)  # Output: PointWithDefaults(x=0, y=0)
print(p2)  # Output: PointWithDefaults(x=5, y=0)
print(p3)  # Output: PointWithDefaults(x=5, y=10)