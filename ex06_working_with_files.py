import os

# 1) Write a short Python script which queries the user for input
# (infinite loop with exit possibility) and writes the input to a file.
var = ''

# initial check to see if file exists, if not it creates the file
with open('response.txt', mode='w') as f:
    f.close()

# input response


def response():
    response = input('What is your secret? ')
    return response

# wrties response to file
# or sets var to q


def make_file():
    global var
    value = response()
    if value != 'q':
        with open('response.txt', mode='a') as f:
            f.write(value)
            f.write('\n')
            f.close()
    else:
        var = value


# loops make_file function, until var == q, then quits the program
while var != 'q':
    print('enter a response, or q to quit!')
    make_file()

os.remove('response.txt')
print("Quitting! File Removed!")
