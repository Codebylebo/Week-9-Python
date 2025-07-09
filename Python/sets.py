# Sets
# Sets are unordered collections of unique elements.
# They are defined by enclosing elements in curly braces or using the `set()` constructor.
# Sets are useful for membership testing and eliminating duplicate entries.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)  # Add an element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)  # Remove an element
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Operations on sets
# Union, intersection, difference, and symmetric difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
# Union adds all elements from both sets, but removes duplicates.
# The result is a new set containing all unique elements from both sets.
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
# Intersection returns a new set containing only elements that are present in both sets/ duplicates.
# The result is a set of common elements.
inter_set = set1.intersection(set2)
print(inter_set)  # Output: {3}

# Difference
# Difference returns a new set containing elements that are in the first set but not in the second.
# The result is a set of elements unique to the first set.
diff_set = set1.difference(set2)
print(diff_set)  # Output: {1, 2}

# Symmetric Difference
# Symmetric difference returns a new set containing elements that are in either set but not in both.
# The result is a set of elements that are unique to each set.
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}

# We can use sets for membership testing, which is efficient. And we can use it to eliminate duplicates from a list.