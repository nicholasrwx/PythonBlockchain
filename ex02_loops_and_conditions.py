# list of names
names = ['John', 'James', 'Jason', 'Jennifer',
         'Joy', 'Joe', 'JuNior', 'Jimmy', 'Jim', 'Jay']


# loop through the names list
for name in names:
    # print name length
    print(str(len(name)))

    # print names with a length greater than 5 that contain 'n' or 'N'
    if len(name) > 5:
        for index in range(len(name)):
            if name[index] == 'n' or name[index] == 'N':
                print(name)
                break


# clear all names from list
while names:
  if len(names) == 1:
    names.pop()
    break
  names.pop()

print('\nthe names list has been cleared:\n\n\t names =', names, '\n')
