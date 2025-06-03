import random


emojis = { 'r': '🪨', 'p': '📄', 's': '✂️' }
choices = ('r', 'p', 's')

def get_user_choice():
    """Get the user's choice and validate it."""
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").strip().lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose 'r', 'p', or 's'.")
            continue
        else:
            return user_choice
                
def display_choices(user_choice, computer_choice):
    """Display the choices made by the user and the computer."""
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices made."""
    if user_choice == computer_choice:
        return "It's a tie! 🤝"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "You win! 🎉"
    else:
        return "You lose! 😢"



def play_game():
# Main game loop
    while True:
    
        user_choice = get_user_choice()
        # Let the computer to make a choice
        # Print choices (emoji)    
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)



        # Determine the winner
        
        determine_winner(user_choice, computer_choice)
        

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        # If not
        #  Terminate the game
        if play_again == 'n':
            print("Thanks for playing! Goodbye! 👋")
            break

play_game()
