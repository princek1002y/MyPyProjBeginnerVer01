import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I have picked a number between 1 and 100. Can you guess what it is?")

    #Generate a random number between 1 and 100
    number_to_guess = random.randint(1,100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Get the user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the user's guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congragulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the game
guess_the_number()