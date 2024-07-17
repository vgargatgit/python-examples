from collections import ChainMap

# Create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Create a ChainMap
cm = ChainMap(dict1, dict2)

print(cm)  # Output: ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})