try:
    age = int(input("age : "))
    print(age)
except ZeroDivisionError:
    print(ZeroDivisionError)
