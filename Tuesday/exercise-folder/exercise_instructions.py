"""
Python Review 2
===============
Create one or more Python files to implement the following game:
 
Ask the user to guess a random number by entering a positive integer (or -1 to quit)
Create a random number between 0 and 100 (e.g. use the following code)
    from random import randint
    r = randint(0,100)
 
When the user types in a number tell them if it's too high or too low (e.g. use a while loop)
When they guess correctly, tell them and stop the program
 
In the game, if the user enters -2 give a clue:
- Is the number even/odd, a square and/or a prime number
- Use your code structures to determine the clues
 
Use functions where needed and aim for efficient code structures. For example you might:
- Create a collection of the even numbers from 0-100
- Create a collection of squares of 0-10
- Create a collection of prime numbers under 100, which are
  (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
 
Optional
--------
Make sure the value entered is a number in the correct range (0-100 or -1 or -2)
Put your functions in a separate file (in a package) and import as needed
Allow the user to choose the number range (and therefore the difficulty)
Give feedback like 'much too small' 'a bit higher', 'close' etc. based on their guess
Suggest a number which would be sensible to guess next, based on their last guess
Store all the guesses in a dictionary
Calculate the average difference between each guess and the random value
At the end, present a report of these data
Offer a 'play again' option and report on high-score and cross-game averages
"""

