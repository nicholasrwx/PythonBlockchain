import os

# 1) Write a short Python script which queries the user for input
# (infinite loop with exit possibility) and writes the input to a file.
# 2) Add another option to your user interface:
# The user should be able to output the data stored in the file in the terminal.
# 3) Store user input in a list (instead of directly adding it to the file)
# and write that list to the file both with pickle and json.
# 4) Adjust the logic to load the file content to work with pickled/ json data.

var = ''
user_input_list = []

# initial check to see if file exists, if not it creates the file
with open('response.txt', mode='w') as f:
    f.close()

# input response


def response():
    response = input('What is your secret? ')
    return response

# wrties response to file
# or sets var to q


def edit_file():
    global var
    value = response()
    if value != 'q':
        with open('response.txt', mode='a') as f:
            f.write(value)
            f.write('\n')
            f.close()
    else:
        var = value


def display_file():
    with open('response.txt', mode='r') as f:
        messages = f.readlines()
        for message in messages:
            print(message[:-1])
        print('\n')
        f.close()

def create_list():
  value = response()
  user_input_list.append(value)
  print(user_input_list)

user_input = True

# loops edit_file function, until var == q, then quits the program
while user_input:
    print('1: write to a file')
    print('2: display file data')
    print('q: quit')
    user_response = input('\n please make your selection: ')
    print('\n')
    if user_response == '1':
        #edit_file()
        create_list()

    if user_response == '2':
        display_file()

    if user_response == 'q':
        user_input = False

os.remove('response.txt')
print("Quitting! File Removed!")



