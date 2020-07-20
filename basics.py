# You can write comments using a # (hash) or a block with """ (three double quotes)
# Module is a different name for a file

# Variables are also called identifiers
a = 7
print(a)

"""
Python won't have major issues with differentiate whole interger and floats
"""

b = 9.3
print(int(b)) # Take the interger of a float (i.e. 9)

print(int(a), b, a+b)

c = '5'
print(int(c)) # Casting a number/interger from a string

"""
Data always has a 'type':

Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
"""

print(type(a), type(b)) # <class 'int'> <class 'float'>

d = "I'm a variable"
c = True # Note booleans need to start with a capital letter (e.g. T for True and F for False)

"""
Rules for identifiers

1. Identifiers may use underscore, strings and/or digits
2. First character CANNOT be a digit
"""

# Math operators ('+, -, *, /')
print(3**3) # Means 'to the power of'
print ('hello ' * 5)

# Divide and truncate
print(9/5) # Division
print(9//5) # Truncation (i.e. divides and prints to the lowest whole value)