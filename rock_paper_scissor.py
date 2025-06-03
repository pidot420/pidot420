import random


emojis = { 'r': '🪨', 'p': '📄', 's': '✂️' }
choices = ('r', 'p', 's')

while True:
    # Ask the user to make a choice
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").strip().lower()
    # If choice is not valid
    #  Print an error message
    if user_choice not in choices:
        print("Invalid choice. Please choose 'r', 'p', or 's'.")

    # Let the computer to make a choice
    # Print choices (emoji)    
    computer_choice = random.choice(choices)

    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")


    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 'p' and computer_choice == 'r') or \
        (user_choice == 's' and computer_choice == 'p'):
        print("You win! 🎉")
    else:
        print("You lose! 😢")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    # If not
    #  Terminate the game
    if play_again == 'n':
        print("Thanks for playing! Goodbye! 👋")
        break

