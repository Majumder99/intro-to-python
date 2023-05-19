# i = 1
# while i<= 5:
#     print(i)
#     i = i + 1

# car game
command = ""
while command != "quit":
    command = input(">").lower()
    if (command == "start"):
        print("car started")
    elif (command == "stop"):
        print("car is stopped")
    else:
        print("I don't understand that")
