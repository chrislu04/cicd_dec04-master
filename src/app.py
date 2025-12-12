import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def logarithm(x, base=10):
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(x, base)

def square(x):
    return x ** 2

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def percentage(value, total):
    if total == 0:
        raise ValueError("Total cannot be zero for percentage calculation")
    return (value / total) * 100
