course = '''hello sourav how are
you'''

# to write multiple line string use ''' ''' double and single won't work

another = course[:]
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:-1])
print(course[0:])
print(another)

# formatted string
first = 'john'
last = "doe"

# for writing variable 'f' should be used
msg = f'{first} [{last}] is a coder'
msg = first + last
print(msg)
