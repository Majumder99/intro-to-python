matrix = [[2, 3, 4], [3, 4, 5], [5, 6, 7]]

for row in matrix:
    for col in row:
        print(col)


# list methods
numbers = [5, 2, 1, 7, 4, 5]
numbers.append(10)
print(numbers)
numbers.insert(2, 30)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.remove(7)
print(numbers)
print(100 in numbers)
print(numbers.count(5))


# unique
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
