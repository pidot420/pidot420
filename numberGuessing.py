import random
number_to_guess = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
attempt = 0
while (guess != number_to_guess & attempt < 5):
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    elif guess == number_to_guess:
        print("Congratulations! You've guessed the number:", number_to_guess)
        break
    attempt += 1
    if attempt >= 5:
        print("Sorry, you've used all your attempts. The number was:", number_to_guess)
        break
    guess = int(input("Guess a number between 1 and 100: "))
    

# This code generates a random number between 1 and 100 and prompts the user to guess it.