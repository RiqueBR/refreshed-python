# Import things at the top

# declare global variables
file_obj = open('sample.txt', 'wt')
file_in = open('data.txt', 'rt')
# wt stands for write text, rt to read text, xt to write text if doesn't exist, 'at' append

# declare global functions
def writeSomething(text):
    file_obj.write(text)

def readFile():
    return file_in.read()

def printToFile(text):
    print(text, file=file_obj)

def tidyUp():
    # Always close file reference
    file_obj.close()
    file_in.close()



# run immediate code
if __name__ == '__main__':
    writeSomething('A bunch of bla bla bla and some other niceties')
    printToFile('print always adds new lines')
    tidyUp()
