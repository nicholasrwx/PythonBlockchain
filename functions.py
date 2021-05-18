#the star operator will take a normal set of args, and turn them into a list 
#*args creates a tuple which you can use in a FOR-loop
#without *args, it would only take a single argument, 
#and would require a list or some sort to be passed,
#in order for the for loop to cycle through it.

# *args <- this is basically unpacking function arguments
# **keyword_args <- this handles dictionaries (key value pairs)


def unlimited_arguments(*args, **keyword_args):
  print(args)
  for argument in args:
    print(argument)
  print(keyword_args)
  for key, value in keyword_args.items():
    print(key, value)


#this will be converted into a tuple
#and the inline variables, will be converted into a dictionary
print('Example 1: \n')
unlimited_arguments(1,2,3,4, name='Max', age=29)

#this will be passed as a single value
print('Example 2: \n')
unlimited_arguments([1,2,3,4])

#this list will be converted into a tuple
print('Example 3: \n')
unlimited_arguments(*[1,2,3,4])

#when args has a star operator, the list needs to be passed with a star also,
#or it will be passed as a single argument.
#it will still print, but it won't iterate through the list.
#it treats multiple arguments passed as a single iterable.


#Above is basically how this works with format and placeholders in a string.
#you can unpack multiple arguments for differen't place holders in a string.
a = [1,2,3]
print('Some text: {} {} {}'.format(*a))
