from collections import deque

# Create a deque
d = deque([1, 2, 3])

# Append to the right end
d.append(4)

# Append to the left end
d.appendleft(0)

print(d)  # Output: deque([0, 1, 2, 3, 4])