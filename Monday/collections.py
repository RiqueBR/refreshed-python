# Exploring strings further but also tuple and lists
# Escaping single quote chars => \' \" \n (new line) \t (tabs) \\(for the slash)

sentence = 'Soon to be lunchtime, I cannot wait!'
print(sentence)

print(sentence[0:20]) # [start: stop-before] or [start: stop-before : step]
print(sentence[::-1]) # default start, default stop, step backwards

"""
A collection is: Collections in python are basically container data types, namely lists, sets, tuples, dictionary. They have different characteristics based on the declaration and the usage.

A tuple is: A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets and can contai different data types.

A set is: A set is a collection which is unordered and un-indexed. In Python sets are written with curly brackets. Sets must have unique members (or values)

A dictionary is: A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

A list is: A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
_____
Mutable collections: 
Lists (also allows duplicate members)
Dictionaries (no duplicate members)

Immutable collections:
Tuples (allows duplicate members)
Sets (no duplicate members)
"""

# Tuples
cities = ('Edinburgh', 'Dublin', 'Bristol', 'Paris', True, 42) # We cannot mutate members of a tuple
print(cities[2], cities[::-1], type(cities))
print(cities[0:4])
print([city for city in cities if type(city) == str]) # Little logic to just print strings in our tuple

# Sets
villages = {'Lennoxtown', 'Cumbernauld', 'Alloa', 'Lenzie'} # Sets can also be created with the keyword set i.e. set(1, 2, 3)
print(villages, type(villages))
for village in villages: # In order to access sets, we must loop through it since sets are non-iterable
  print(village)
# It is preferable to declare a set with the keyword set instead of just curly brackets in order to not get confused with dictionaries

# Dictionaries
clubs = {
  1: {'name': 'Liverpool FC', 'country': 'England'},
  2: {'name': 'Corinthians FC', 'country': 'Brazil'}
}

print(clubs)
print(clubs[1]['name']) # Dictionaries are accessed by its name not indexes!!!
print(clubs[2]['country'])

# Lists
# Mutable and zero-based index. Members do not need to be the same type
menu = ['apple', 'cheese', 'banana', 'crisps', 'lettuce']
menu[3] = 'onion' # Mutable members
print(menu[1], menu[3], menu[0:3])

print('apple' in menu, 'orange' in menu)
print(menu.index('cheese'))

## Using conditional logic
if 'apple' in menu:
  print("We've got apples yo!")

searchterm = input('What are you looking for? ')
if searchterm in menu:
  print('We have', searchterm, 'at position', menu.index(searchterm))
else:
  print("We don't have", searchterm)


# Data modelling - How and when to use collections
"""
In MVC situations i.e. See the situation below
Imagine a username(first, last, passoword), monitor(time, timeout, firstlogin), pages. Let's create a collection
"""

online = [('Bob', 'Bloggs', 'bob123'), {'time': 0, 'timeout': 180, 'firstlogin': True}, []]

# Accessing and mutating members of our collection
print(online[0][2])

online[1]['time'] = 60
print(online[1]['time'])

online[1]['firstlogin'] = False
print(online[1]['firstlogin'])

online[2] = ['Home']
online[2].append('Contact us')
print(online[2])