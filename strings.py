# Let's have a look at strings, Strings are immutable by nature

username = 'Bob'

print(username)
print(username[0]) # String collections are indexed like an array e.g. 0, 1, 2, 3...
# we cannot alter a character in a string i.e.
# username[0] = '0' this will cause an error for the reason above

"""
A tuple is:
A set is:
A collection is:
"""


# Tuples are immutable
myTuple = ('Python', 'ECMAScript', 'Java', 'Ruby')
print(myTuple[3])

# myTuple[1] = 'Javascript'
# print(myTuple[1]) => This will error, we cannot mutate members of a tuple

username = input('Please type your username:')
print('Your new username is', username)
print('There are', len(username), 'characters in your name. Now you know ;)')