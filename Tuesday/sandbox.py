# Clean up incoming data, so we are sure it is a 'str' and capitalized

def cleanup(data):
    # Reusable function to capitalise
    def makeCaps(value):
        value = value.capitalize()
        return value
    # Check the type
    if type(data) == 'str':
        data = makeCaps(data)
    else:
        data = str(data)
        data = makeCaps(data)
    
    return data

if __name__ == '__main__':
    val = 'Henry'
    print(cleanup(val), type(cleanup(val)))

    val = True
    print(cleanup(val), type(cleanup(val)))

    val = 12345
    print(cleanup(val), type(cleanup(val)))