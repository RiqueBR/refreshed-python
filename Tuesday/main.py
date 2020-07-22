# Importing our code from a different module (or file)
# import sandbox # This way imports the entire module

from sandbox import cleanup # Only imports the necessary function

# importing a file (e.g. file) from a package (e.g. folder)
from package.module import addValues

# The following wil only run if this is the main module (not if it's been imported)
if __name__ == '__main__':
    value = cleanup('lol')
    print(value)

    print(addValues(2.45, 46, 908, 78.92379823))


"""
The reason for adding the statement of name == main is to avoid including globals on imported modules.
Globals from modules are dictionaries, which means that importing modules would import the entirety of the contents of such module.
This increases robustness of our code and allows us to safeguard our modules.
"""