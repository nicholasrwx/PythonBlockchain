import json
import pickle

user_input_list = []


def response():
    response = input('What is your secret? ')
    return response

# writes response to file


def edit_file(messages):
    with open('response.txt', mode='w') as f:
        f.write(json.dumps(messages))
        f.close()
    with open('response.p', mode='wb') as f:
        f.write(pickle.dumps(messages))
        f.close()


def display_file():
    with open('response.txt', mode='r') as f:
        values = f.readlines()
        messages = json.loads(values[0])
        print('.txt File Content:\n')
        [print(message) for message in messages]
        print('\n')
        f.close()
    with open('response.p', mode='rb') as f:
        values = pickle.loads(f.read())
        print(".p File Content:\n")
        [print(value) for value in values]
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
        # edit_file()
        create_list()

    if user_response == '2':
        display_file()

    if user_response == 'q':
        if len(user_input_list) > 0:
            edit_file(user_input_list)
        user_input = False
