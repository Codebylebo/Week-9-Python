# Dictionary in Python
# Creating a dictionary
# A dictionary is a collection of key-value pairs, where each key is unique.
# Dictionaries are defined using curly braces `{}` or the `dict()` constructor.
# They are useful for storing data that can be accessed via keys.

my_dict = {'apple' : 3, 'banana' : 5, 'orange' : 2}
print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 2}

# Accessing values
print(my_dict['apple'])  # Output: 3

# Adding or updating key-value pairs
my_dict['grape'] = 4
print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 2, 'grape': 4}

# modifying an existing key-value pair
my_dict['banana'] = 6
print(my_dict)  # Output: {'apple': 3, 'banana': 6, 'orange': 2, 'grape': 4}