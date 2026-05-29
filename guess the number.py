import random
computer_number = random.randint(1, 10)
user_number = int(input("Enter a number between 1 and 10:"))
while user_number != computer_number:
    if user_number < computer_number:
        user_number = int(input("too low! try again:"))
    else:
        user_number = int(input("too high! try again:"))
print("Congratulations! You guessed the number!")
      