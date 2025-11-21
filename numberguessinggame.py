import random

def maryam_guess_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        number_to_guess = random.randint(1, 50)
        attempts = 0
        print("\nI have selected a number between 1 and 50. Can you guess it?")
        
        while True:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < 1 or user_guess > 50:
                print("Please guess a number between 1 and 50.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the number in {attempts} attempts.")
                break
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Run the game
maryam_guess_game()
