### Scope: everything outside of a block is i the global scope
my_global = 'this is a global variable/identifier'

if city == '':
  flag = 'empty' # flag is inside the scope

print(my_global)
print(flag) # This will cause an error, saying it's undefined