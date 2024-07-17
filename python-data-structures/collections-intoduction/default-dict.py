from collections import defaultdict

# Create a defaultdict with list as the default factory
dd = defaultdict(list)
dd['a'].append(1)
dd['b'].append(2)

print(dd)  # Output: defaultdict(<class 'list'>, {'a': [1], 'b': [2]})