from point import Point

p1 = Point._make([10, 20])

p_dict = p1._asdict()
print(p_dict)  # Output: OrderedDict([('x', 10), ('y', 20)])