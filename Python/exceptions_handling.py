# Exceptions handling in Python
# Exceptions are events that can modify the flow of a program.
# They can be raised by the interpreter or by the programmer.

"""try:
    print(x)""" # This will raise an exception because x is not defined
"""
except NameError:
    print("A NameError occurred: x is not defined")
except:
    print("An exception occurred: x is not defined")"""
    
"""try:
    print(x) 
except:
    print("Something went wrong")""" #This will catch any exception that occurs in the try block
"""finally:
    print("The 'try-except' block has finished")"""
    # the finally block will always execute, regardless of whether an exception was raised or not
    
#the else block can be used to execute code if no exceptions were raised
"""try:
    print(Hello)"""  # This will raise a NameError because Hello is not defined
"""except NameError:
    print("A NameError occurred")
else:
    print("No exceptions were raised")"""

x = -1

if x < 0:
    raise ValueError("x must be a non-negative number")  # This will raise a ValueError if x is negative
