# Modelling data

# It's possible to mix dictionaries with lists, and tuples, sets and so on...
dictionary = { 'numbers': [1, 2, 3], 'other': (7, 8, 9), 'myList': [(), [], []] }

"""
Generators: Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

Comprehension: List comprehension is an elegant way to define and create lists based on existing lists.
"""

for i in range(1, 999, 3): # I'm generating a bunch of values i.e. using a generator
  print(id(i), i)

my_list = [n for n in range(1, 99)] # A list comprehension, generating values
my_tuple = (n for n in range(1, 99))

print(my_list)
print(my_tuple)