f = open('demo.txt', mode='w')
f.write('Hello from Python!') 
# you need to call close, 
# otherwise it wont write to the file 
# until the program has ended
f.close()

user_input = input('Please enter input: ')
