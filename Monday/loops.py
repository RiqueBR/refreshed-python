# Imports
# Python includes a set of useful libraries we can import


# from random import randint
import random
for i in range(0, 100):
  print(random.randint(0,10))

# Using conditionals
num = 110

if num < 100:
  print('Under 100')
elif num > 100: # Known in another languages as else if
  print('Over 100')
else:
  print('not sure...')

if num > 0 and num < 10:
  print('Between 0 and 10')
elif num > 100 or num < 0:
  print('Either greater than 100 or negative')

# Comparison operators (<= >= != ==)
# NB to check equality we must use ==

for i in range(1, 10, 2): # start, stop-before, step-over/skip
  print(i)

cities = ('Glasgow', 'Edinburgh', 'St Andrews')
for city in cities:
  print(city)
  # break # Used for breaking out of a loop

print(city)

