from random import randint, uniform
from datetime import date


#generate a random number between 0 and 1
print('{}, <- BETWEEN 0 & 1'.format(uniform(0.01, 0.99)))
#generate a random number between 1 and 10
value = str(randint(2,9))
print(value, ' <- BETWEEN 1 & 10')

current_date = str(date.today())
print(current_date, ' <- CURRENT-DATE')

appended = '{}'.format(current_date + value)
print(appended, ' <- CURRENT-DATE + VALUE BETWEEN 1 & 10')




