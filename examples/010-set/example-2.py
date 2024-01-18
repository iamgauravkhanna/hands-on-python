set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union of sets
union_set = set1 | set2  # or use set1.union(set2)
print(union_set)         # Output: {1, 2, 3, 4, 5, 6, 7}

# Intersection of sets
intersection_set = set1 & set2  # or use set1.intersection(set2)
print(intersection_set)         # Output: {3, 4, 5}

# Difference of sets
difference_set = set1 - set2  # or use set1.difference(set2)
print(difference_set)         # Output: {1, 2}