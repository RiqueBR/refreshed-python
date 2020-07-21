# Looping with the 'while' keyword

while True: # also known as run-loop
  m = input('What next? ')
  if m == 'q':
    break
  else:
    print(m.capitalize())