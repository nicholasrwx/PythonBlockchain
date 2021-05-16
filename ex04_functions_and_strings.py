# 1) Write a normal function that accepts another function as an argument. 
# Output the result of that other function in your “normal” function.

#Normal function, takes two args -> A Function and A Value
def normal_function(*args):
  
  func, *value = args
  
  for el in value:
    result = func(el)
    print('{:-^20.2f}'.format(result))

#Function -> for argument
def test_func(arg):
  return arg + 5

#Call normal_function & pass it a function & a value
normal_function(test_func, 2)




# 2) Call your “normal” function by passing a lambda function – 
# which performs any operation of your choice – as an argument.

#passing a lambda & a value
normal_function(lambda arg: arg + 10, 2)



# 3) Tweak your normal function by allowing an infinite amount 
# of arguments on which your lambda function will be executed.     

normal_function(lambda arg: arg + 10, *[2,3,4,5,6,7,8])


# 4) Format the output of your “normal” function such that numbers 
# look nice and are centered in a 20 character column.
#print('{:-^20}'.format(result))  ->  ✓
