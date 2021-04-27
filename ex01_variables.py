#this needs to run with python3, otherwise 
#In Python 2, getting input as plain text is done via raw_input instead of input. 
#The Python 2 version of input does eval(raw_input(prompt)), 

def name():
  return input('What is your name? ')


def age():
  return input('What is your age? ')


def decades(age):
  total = float(age) / 10
  return str(total)


name = name()
age = age()
result = name + ' is ' + age + ', and has lived ' + decades(age) + ' decades.'

print(result)
