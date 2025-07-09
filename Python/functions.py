# Functions
# Functions are reusable pieces of code that can be called multiple times.
# They can take inputs (arguments) and return outputs (return values).
# Functions help to organize code, make it more readable, and avoid repetition.

def greet(name):
    print(f"Hello, {name}!")
    
greet("Alice")


def add(a, b):
    #Returns the sum of two numbers.
    return a + b

result = add(2, 5)
print(result)  # Output: 7

def factorial(n):
    #Returns the factorial of a number.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # Factorial function calls itself recursively

def greet(name, greeting="Hello"):
    #Greets a person with a specified greeting.
    print(f"{greeting}, {name}!")
    
    
greet("Bob", "Good Morning")  # Output: Hello, Bob!