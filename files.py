# f = open('demo.txt', mode='w')
# f.write('Hello from Python!') 
# # you need to call close, 
# # otherwise it wont write to the file 
# # until the program has ended
# f.close()
# user_input = input('Please enter input: ')



# #read only (if demo.txt doesn't exist, nothing will be displayed)
# f = open('demo.txt', mode='r')
# file_content = f.read()
# print(file_content)
# f.close()



# #open an existing file, and append something to it
# f = open('demo.txt', mode='a')
# f.write('Something\n')
# f.close()



# read() always reads the entire file, 
# where as readlines(), reads each line as separate, 
# and will space them into a comma separated LIST.

# f = open('demo.txt', mode='r')
# file_content = f.readlines()
# f.close()
# for line in file_content:
#   print(line[:-1]) 


#readline() just reads a single line of the file.
f = open('demo.txt', mode='r')
print(f.readline())












