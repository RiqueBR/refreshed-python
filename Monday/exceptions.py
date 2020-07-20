startnum = 10

try:
  addNum = input('Increment by how much? ')
  print(startnum + addNum) # Issue here is we cannot sum a string and a number
except:
  # We break the process here if there's an issue
  print('Oh dear, what happened?')
finally:
  print('Better luck next time')
