#DATA STRUCTURES

simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
del(simple_list[0])
print(simple_list)


# Dictionary
d = {'name': 'Max'}
print(d.items())
for k, v in d.items():
    print(k, v)
del(d['name'])
print(d)


# Del() DOESN'T WORK for tuples and sets

# Tuple
t = (1, 2, 3)
print(t.index(1))
# del(t[0])
print(t)


# Set
s = {'Max', 'Anna', 'Max'}
# del(s['Max'])
print(s)
