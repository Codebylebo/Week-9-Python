# Tuples. Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Tuples are defined by enclosing elements in parentheses, separated by commas.
# Example of a tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
# Accessing elements in a tuple

print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2
print(my_tuple[2])  # Output: 3 

# Negative indexing in a tuple
print(my_tuple[-1])  # Output: 5
print(my_tuple[-2])  # Output: 4
print(my_tuple[-3])  # Output: 3

# concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
conc_tuple = tuple1 + tuple2
print(conc_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
rep_tuple = tuple1 * 3
print(rep_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)