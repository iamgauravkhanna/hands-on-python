# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}

# Creating a set using the set() constructor
another_set = set([3, 4, 5, 6, 7])

# Sets automatically remove duplicate elements
duplicate_set = {1, 2, 2, 3, 3, 4, 4, 5, 5}

print(my_set)           # Output: {1, 2, 3, 4, 5}
print(another_set)      # Output: {3, 4, 5, 6, 7}
print(duplicate_set)    # Output: {1, 2, 3, 4, 5}
