import random

# Loop
while True:
    choice = input("Roll the dice? (y/n): ").strip().lower()
    # If user enters y
     #    Generate two random numbers between 1 and 6
     #    Print them
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled: {dice1} and {dice2}")
    # If user enters n
     #    Print Thank You message
     #    Terminate the program
    elif choice == 'n':
        print("Thank you for playing!")
        break
    # Else
     #    Print Invalid input message
    else:
        print("Invalid input. Please enter 'y' to roll or 'n' to exit.")
 
 
