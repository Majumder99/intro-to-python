names = ['john', 'mosh', 'sourav', 'majumder', 'ssdjfsjdfak;sljd f']

print(names)
print(names[-1])
print(names[2:])
print(names[:-1])
names[0] = 'gadha'
print(names)


# largest number
lenght = len(names[0])
big = ''
for x in names:
    m = len(x)
    if (m > lenght):
        lenght = m
        big = x
print("biggest is", x)
