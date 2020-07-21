# We declare functions by using the 'def' keyword

def addNums(x, y): # Positional arguments
  return x + y

addNums(3, 5)

def anotherAddition(x=1, y=2): # You can also provide default values
  return x + y

anotherAddition(y=6, x=2) # Overriding params

# args and kwargs

def other(*args): # *args collects all positional arguments into a tuple
  return args

print(other(42, 'coffee', True, []))

def addAll(*args):
  total = 0
  for item in args:
    total = total + item
  return total

print(addAll(1, 2, 3, 4, 5))

def nameList(**kwargs): # **kwargs is the collection of keyword arguments
  print(kwargs)

nameList(Ada='UK', Georg='Ukraine', Baird='Scot', Dermot='IE')

# We are able to mix args and kwargs in the same function
def addAllTypes(*args, **kwargs):
  print(args, kwargs)

addAllTypes(42, 'Ethel', [True, False], id = 12345, key='unlock', currentLocation = {'city': 'Edinburgh'})