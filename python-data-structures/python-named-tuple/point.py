from collections import namedtuple

# Define a namedtuple called Point
Point = namedtuple('Point', ['x', 'y'])

if __name__ == '__main__':

    # Create instances of Point
    p1 = Point(10, 20)
    p2 = Point(x=30, y=40)

    print(p1)  # Output: Point(x=10, y=20)
    print(p2)  # Output: Point(x=30, y=40)

    print(f'p1.x = {p1.x}')  # Output: p1.x = 10
    print(f'p1.y = {p1.y}')  # Output: p1.y = 20
    print(f'p1[0] = {p1[0]}')  # Output: p1[0] = 10
    print(f'p1[1] = {p1[1]}')  # Output: p1[1] = 20