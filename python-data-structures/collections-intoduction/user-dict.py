from collections import UserDict, UserList, UserString

# Create a custom dictionary
class MyDict(UserDict):
    def __missing__(self, key):
        return 'default value'

md = MyDict({'a': 1})
print(md['a'])  # Output: 1
print(md['b'])  # Output: default value