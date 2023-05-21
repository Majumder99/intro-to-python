import random

print(random.random() * 1000)
print(random.randint(10, 20))


members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)
