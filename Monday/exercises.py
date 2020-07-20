months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

print(months.index('Apr')) # index = 3
print(months[6:9])

firstname = input('What is your first name? ')
lastname = input('And what is your last name? ')
dobDay = input('What day were you born? ')
dobMonth = input('What month were you born? (Please as a three letter acronym, e.g. "Jan") ')
dobYear = input('What year were you born? ')

monthNum = months.index(dobMonth) +1
separator = '/'
dob = separator.join([dobDay, str(monthNum), dobYear])

print('Thanks for answering those questions', firstname)
print('Can you confirm the following, Your full name is:', firstname + '' + lastname, 'Born on', dob)

firstname = input('Type you firstname all in lower case, please ')
lastname = input('Type you lastname all in lower case, please ')

fullname = " ".join([firstname, lastname])
# print(firstname.title(), firstname[::-1])
print(fullname)

middleName = input('What is your middle name? ')
fullname = " ".join([firstname, middleName, lastname])
print(fullname)
