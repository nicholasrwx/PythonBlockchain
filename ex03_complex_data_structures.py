# 1 list of person dictionaries -> each person has a name, age, and hobbies key. hobbies value is a list of str's
person = [{'name': 'Jane', 'age': 20, 'hobbies': ['tennis', 'swimming', 'nascar']},
          {'name': 'Dennis', 'age': 25, 'hobbies': [
              'base jumping', 'dirtbiking', 'karate in the garage']},
          {'name': 'Karen', 'age': 35, 'hobbies': [
              'voicing unwanted opinions', 'hot gossip', 'over applying make-up on the train', 'sarcasm']},
          {'name': 'Linda', 'age': 40, 'hobbies': [
              'tea', 'classical music', 'witty banter']},
          {'name': 'Roy', 'age': 29, 'hobbies': ['heavy metal', 'trucks', 'bbq and beers with the boys']}]

print('person list:\n')
print(person, '\n\n')


# 2 use list comprehension to convert person_list[name] names into a list of names
list_of_persons = [el['name'] for el in person]
print('list of person names:\n')
print(list_of_persons, '\n\n')


# 3 use list comprehension to check whether all persons are older than 20
all_persons = all([el['age'] > 20 for el in person])
print('are all persons over 20?:\n')
print(all_persons, '\n\n')


# 4 copy the person list such that you can safely edit the name of the first persons list
print('original list of persons:\n', list_of_persons, '\n\n')
list_of_persons_copy = list_of_persons[:]
list_of_persons_copy[0] = 'Brock'
print('edited copy of original list:\n', list_of_persons_copy, '\n\n')
print('original list of persons remains unaltered:\n', list_of_persons, '\n\n')


# 5 unpack the persons of the original list into different vars and output them
values = (P1, P2, P3, P4, P5) = person

[print(el) for el in values]
