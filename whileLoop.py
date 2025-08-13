# number = 100
# while (number < 110):
#     print(number)
#     number += 1


command = ""
while command.lower() != "quit":
    command = input("Enter a command (type 'quit' to exit): ")
    print(f"You entered: {command}")
