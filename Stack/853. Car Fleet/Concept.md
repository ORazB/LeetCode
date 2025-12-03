# Questions:
# Why do we need to sort it in reverse order?
# Because we want to process the cars starting from the one closest to the target to the farthest.

# Why do we update currentTime only when we find a slower car?
# Because a car that takes longer to reach the target cannot catch up to a car that is already ahead of it.

# Counter vs Stack
# In counter we just count the fleets when we find a slower car
# In stack we actually store the time taken for each fleet and compare them


# New function: zip()
# The zip() function in Python takes iterables (can be zero or more), combine them in a tuple, and returns it.
# Example: zip([1, 2, 3], ['a', 'b', 'c']) returns [(1, 'a'), (2, 'b'), (3, 'c')]
# Here, we use zip to pair each car's position with its speed.

# Using .index() would be inefficient here as it would lead to O(N^2) complexity in the worst case.
# And also, if there are duplicate positions, .index() would not work correctly.