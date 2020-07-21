def addValues(*args):
    total = 0
    for n in args:
        if type(n) == int or type(n) == float:
            total += n
    return total

if __name__ == '__main__':
    print(addValues(1, 2.5, 938723.7473))